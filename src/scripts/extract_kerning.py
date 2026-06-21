#!/usr/bin/env python3
"""Extract pair kerning from a TTF.

Reads pair kerning from the font's GPOS `kern` feature (both Format 1
glyph pairs and Format 2 class-based pairs, including Extension lookups) and
from the legacy `kern` table, keeping pairs whose horizontal adjustment is
non-zero. By default only pairs where BOTH glyphs are ASCII letters or digits
(a-z / A-Z / 0-9) are kept; pass --all to widen the set to alphanumerics plus
the special signs defined in the project (glyphs/special and glyphs/extra:
punctuation, symbols and dashes). Both glyphs of a pair must be in the set.

Usage:
    python src/scripts/extract_kerning.py path/to/font.ttf
    python src/scripts/extract_kerning.py path/to/font.ttf --all
    python src/scripts/extract_kerning.py path/to/font.ttf --csv out.csv
    python src/scripts/extract_kerning.py path/to/font.ttf --dict
    python src/scripts/extract_kerning.py path/to/font.ttf --side-bearing 68
"""

import argparse
import csv
import os
import re
import string

from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen

KERN_CHARS = set(string.ascii_letters + string.digits)

# Project glyph categories that count as "special signs" (punctuation/symbols).
SPECIAL_GLYPH_DIRS = ("special", "extra")


def project_special_chars():
    """Characters defined by the project's glyphs/special and glyphs/extra modules.

    Each glyph module declares e.g. ``unicode = "0x2E"``; we read those without
    importing the heavy drawing dependencies. Returns an empty set if the source
    tree can't be located (e.g. the script was copied out of the project).
    """
    base = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "glyphs"
    )
    chars = set()
    for sub in SPECIAL_GLYPH_DIRS:
        d = os.path.join(base, sub)
        if not os.path.isdir(d):
            continue
        for fn in os.listdir(d):
            if not fn.endswith(".py") or fn == "__init__.py":
                continue
            with open(os.path.join(d, fn)) as fh:
                m = re.search(r'unicode\s*=\s*"(0x[0-9A-Fa-f]+)"', fh.read())
            if m:
                chars.add(chr(int(m.group(1), 16)))
    return chars


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


def _pair_label(a, b):
    """Compact label for a pair: 'AV' for single chars, 'space-joined' otherwise."""
    return a + b if len(a) == 1 and len(b) == 1 else f"{a} {b}"


def extract_kerning(font, all_glyphs=False):
    """Return {(char1, char2): value} for pairs with non-zero kerning.

    By default only ASCII letter/digit pairs are kept. With all_glyphs=True the
    set is widened to alphanumerics plus the special signs defined in the
    project (glyphs/special and glyphs/extra); both characters of a pair must
    still be in that set.
    """
    allowed = set(KERN_CHARS)
    if all_glyphs:
        allowed |= project_special_chars()

    cmap = font.getBestCmap()
    # glyph name -> character, restricted to the allowed set
    char_by_glyph = {}
    for cp, gname in cmap.items():
        ch = chr(cp)
        if ch in allowed:
            char_by_glyph.setdefault(gname, ch)
    label = char_by_glyph
    kern_glyphs = set(label)

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
        result[(label[g1], label[g2])] = val
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Extract pair kerning from a TTF (letters/digits by default, all glyphs with --all)."
    )
    parser.add_argument("font", help="Path to a TTF font file")
    parser.add_argument(
        "--all",
        action="store_true",
        help="Widen from letters/digits to alphanumerics + the project's special "
        "signs (glyphs/special and glyphs/extra: punctuation, symbols, dashes)",
    )
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
    kerning = extract_kerning(font, all_glyphs=args.all)
    units = font["head"].unitsPerEm
    l_sb = letter_side_bearing(font, "l")

    scope = "all" if args.all else "letter/digit"
    print(f"Font: {args.font}  (unitsPerEm={units})")
    if l_sb is not None:
        print(f"Lowercase 'l' side bearing: {l_sb:.0f}")
    print(f"{scope} kerning pairs found: {len(kerning)}\n")

    if not kerning:
        print("No kerning found (no GPOS 'kern' pairs or legacy 'kern' table).")
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
        pair = _pair_label(a, b)
        line = f"{pair:>4}  {val:>6.0f}"
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
        csv_rows.append([pair, f"{val:.0f}"] + extra)

    if args.dict:
        if not has_l:
            parser.error("--dict needs a usable 'l' glyph to express kerning as a ratio")
        print("\n{")
        for (a, b), val in rows:
            print(f'    "{_pair_label(a, b)}": {val / l_sb:.2f},')
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
