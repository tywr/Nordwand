#!/usr/bin/env python3
"""Extract kerning between letter and number pairs from a TTF.

Reads pair kerning from the font's GPOS `kern` feature (both Format 1
glyph pairs and Format 2 class-based pairs, including Extension lookups) and
from the legacy `kern` table, then keeps only pairs where BOTH glyphs are
ASCII letters or digits (a-z / A-Z / 0-9) and the horizontal adjustment is
non-zero.

Usage:
    python src/scripts/extract_kerning.py path/to/font.ttf
    python src/scripts/extract_kerning.py path/to/font.ttf --csv out.csv
    python src/scripts/extract_kerning.py path/to/font.ttf --dict
    python src/scripts/extract_kerning.py path/to/font.ttf --side-bearing 68
"""

import argparse
import csv
import string

from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

KERN_CHARS = set(string.ascii_letters + string.digits)


def letter_side_bearing(font, char="l"):
    """Left side bearing (x_min of the outline) of `char`, or None if absent/empty."""
    cmap = font.getBestCmap()
    cp = ord(char)
    if cp not in cmap:
        return None
    name = cmap[cp]
    glyph_set = font.getGlyphSet()
    if name not in glyph_set:
        return None
    pen = BoundsPen(glyph_set)
    glyph_set[name].draw(pen)
    if pen.bounds is None:
        return None
    return pen.bounds[0]  # x_min; 'l' is a symmetric stem so LSB == RSB


def _xadvance(value):
    """Horizontal advance adjustment of a GPOS ValueRecord (0 if absent)."""
    if value is None:
        return 0
    return getattr(value, "XAdvance", 0) or 0


def _class_groups(classdef, domain):
    """Map class value -> [glyph names], restricted to `domain` (a set)."""
    defs = classdef.classDefs if classdef is not None else {}
    groups = {}
    for g in domain:
        groups.setdefault(defs.get(g, 0), []).append(g)
    return groups


def _pairs_from_subtable(sub, kern_glyphs):
    """Yield (glyph1, glyph2, xadvance) from one PairPos subtable."""
    if sub.Format == 1:
        for g1, pairset in zip(sub.Coverage.glyphs, sub.PairSet):
            if g1 not in kern_glyphs:
                continue
            for pvr in pairset.PairValueRecord:
                if pvr.SecondGlyph not in kern_glyphs:
                    continue
                val = _xadvance(pvr.Value1)
                if val:
                    yield g1, pvr.SecondGlyph, val
    elif sub.Format == 2:
        cov = [g for g in sub.Coverage.glyphs if g in kern_glyphs]
        g1_groups = _class_groups(sub.ClassDef1, cov)
        g2_groups = _class_groups(sub.ClassDef2, kern_glyphs)
        for c1, g1s in g1_groups.items():
            rec1 = sub.Class1Record[c1]
            for c2, g2s in g2_groups.items():
                val = _xadvance(rec1.Class2Record[c2].Value1)
                if not val:
                    continue
                for g1 in g1s:
                    for g2 in g2s:
                        yield g1, g2, val


def _kern_subtables(gpos):
    """Yield PairPos (type 2) subtables reached by the 'kern' feature."""
    if gpos is None:
        return
    table = gpos.table
    if not table.LookupList or not table.FeatureList:
        return
    kern_lookups = set()
    for frec in table.FeatureList.FeatureRecord:
        if frec.FeatureTag == "kern":
            kern_lookups.update(frec.Feature.LookupListIndex)
    for idx in sorted(kern_lookups):
        lookup = table.LookupList.Lookup[idx]
        for sub in lookup.SubTable:
            lt = lookup.LookupType
            if lt == 9:  # Extension: unwrap
                lt = sub.ExtensionLookupType
                sub = sub.ExtSubTable
            if lt == 2:
                yield sub


def extract_kerning(font):
    """Return {(char1, char2): value} for letter pairs with non-zero kerning."""
    cmap = font.getBestCmap()
    # glyph name -> character (ASCII letters and digits only)
    char_by_glyph = {}
    for cp, gname in cmap.items():
        ch = chr(cp)
        if ch in KERN_CHARS:
            char_by_glyph.setdefault(gname, ch)
    kern_glyphs = set(char_by_glyph)

    pairs = {}  # (g1, g2) -> value ; GPOS wins over legacy kern

    gpos = font.get("GPOS")
    for sub in _kern_subtables(gpos):
        for g1, g2, val in _pairs_from_subtable(sub, kern_glyphs):
            pairs[(g1, g2)] = val

    # Legacy `kern` table (format 0), only if not already covered by GPOS.
    if "kern" in font:
        for st in font["kern"].kernTables:
            for (g1, g2), val in getattr(st, "kernTable", {}).items():
                if g1 in kern_glyphs and g2 in kern_glyphs and val:
                    pairs.setdefault((g1, g2), val)

    result = {}
    for (g1, g2), val in pairs.items():
        result[(char_by_glyph[g1], char_by_glyph[g2])] = val
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Extract lowercase/uppercase letter-pair kerning from a TTF."
    )
    parser.add_argument("font", help="Path to a TTF font file")
    parser.add_argument("--csv", metavar="FILE", help="Write the pairs as CSV")
    parser.add_argument(
        "--dict",
        action="store_true",
        help='Print a copy-pasteable Python dict ({"AV": -40, ...})',
    )
    parser.add_argument(
        "--side-bearing",
        type=float,
        metavar="N",
        help="Also show each value as a fraction of N (e.g. the project side_bearing)",
    )
    args = parser.parse_args()

    font = TTFont(args.font)
    kerning = extract_kerning(font)
    units = font["head"].unitsPerEm
    l_sb = letter_side_bearing(font, "l")

    print(f"Font: {args.font}  (unitsPerEm={units})")
    if l_sb is not None:
        print(f"Lowercase 'l' side bearing: {l_sb:.0f}")
    print(f"Letter-pair kerns found: {len(kerning)}\n")

    if not kerning:
        print("No letter-pair kerning found (no GPOS 'kern' pairs or legacy 'kern' table).")
        font.close()
        return

    rows = sorted(kerning.items(), key=lambda kv: (kv[0][0], kv[0][1]))

    has_l = l_sb not in (None, 0)
    has_sb = args.side_bearing not in (None, 0)
    header = ["pair", "value"] + (["/l"] if has_l else []) + (["/sb"] if has_sb else [])
    print(
        f"{'pair':>4}  {'value':>6}"
        + (f"  {'/l':>6}" if has_l else "")
        + (f"  {'/sb':>6}" if has_sb else "")
    )
    print(
        f"{'----':>4}  {'-----':>6}"
        + (f"  {'-----':>6}" if has_l else "")
        + (f"  {'-----':>6}" if has_sb else "")
    )
    csv_rows = []
    for (a, b), val in rows:
        line = f"{a + b:>4}  {val:>6.0f}"
        extra = []
        if has_l:
            rl = f"{val / l_sb:.2f}"
            line += f"  {rl:>6}"
            extra.append(rl)
        if has_sb:
            rsb = f"{val / args.side_bearing:.2f}"
            line += f"  {rsb:>6}"
            extra.append(rsb)
        print(line)
        csv_rows.append([a + b, f"{val:.0f}"] + extra)

    if args.dict:
        if not has_l:
            parser.error("--dict needs a usable 'l' glyph to express kerning as a ratio")
        print("\n{")
        for (a, b), val in rows:
            print(f'    "{a}{b}": {val / l_sb:.2f},')
        print("}")

    if args.csv:
        with open(args.csv, "w", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(header)
            writer.writerows(csv_rows)
        print(f"\nWrote {len(csv_rows)} rows to {args.csv}")

    font.close()


if __name__ == "__main__":
    main()
