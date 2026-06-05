#!/usr/bin/env python3
"""Tabulate advance width and side bearings for the main glyphs of a TTF.

Reads metrics straight from the font (so it works on any TTF, not just this
project's output):

  * advance width   -- from the `hmtx` table
  * left side bearing  (LSB) -- x_min of the glyph outline
  * right side bearing (RSB) -- advance - x_max of the glyph outline

and two normalized columns:

  * w/o   -- advance width relative to lowercase 'o'
  * LSB/l, RSB/l -- side bearings relative to lowercase 'l'

Usage:
    python src/scripts/glyph_metrics.py path/to/font.ttf
    python src/scripts/glyph_metrics.py path/to/font.ttf --csv out.csv
"""

import argparse
import csv
import string
import unicodedata

from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen


# Main glyph set, grouped like the project. Only characters actually present
# in the font's cmap are reported.
GROUPS = {
    "Lowercase": list(string.ascii_lowercase),
    "Uppercase": list(string.ascii_uppercase),
    "Numbers": list(string.digits),
    "Special": list(
        ".,:;!?"  # punctuation
        "'\""  # quotes
        "-_/\\|"  # dashes / slashes / bar
        "()[]{}"  # brackets
        "<>=+*"  # math-ish
        "&@#%$~"  # symbols
        "—–°"  # em dash, en dash, degree
        "æœøßÆŒØ"  # æ œ ø ß Æ Œ Ø
    ),
}

REF_WIDTH_CHAR = "o"  # advance widths are reported relative to this
REF_SB_CHAR = "l"  # side bearings are reported relative to this


def x_bounds(glyph_set, glyph_name):
    """Return (x_min, x_max) of a glyph's outline, or None if it has no ink."""
    if glyph_name not in glyph_set:
        return None
    pen = BoundsPen(glyph_set)
    glyph_set[glyph_name].draw(pen)
    if pen.bounds is None:
        return None
    return pen.bounds[0], pen.bounds[2]


def measure(glyph_set, hmtx, cmap, ch):
    """Return a metrics dict for character `ch`, or None if absent/empty."""
    code = ord(ch)
    if code not in cmap:
        return None
    name = cmap[code]
    advance = hmtx[name][0]
    bounds = x_bounds(glyph_set, name)
    if bounds is None:
        # No outline (e.g. a blank glyph): side bearings are undefined.
        return {"char": ch, "advance": advance, "lsb": None, "rsb": None}
    x_min, x_max = bounds
    return {
        "char": ch,
        "advance": advance,
        "lsb": x_min,
        "rsb": advance - x_max,
    }


def _ratio(value, ref):
    if value is None or ref in (None, 0):
        return None
    return value / ref


def _fmt_num(value):
    return "-" if value is None else f"{value:.0f}"


def _fmt_ratio(value):
    return "-" if value is None else f"{value:.2f}"


def main(s=174):
    parser = argparse.ArgumentParser(
        description="Tabulate width and side bearings for the main glyphs of a TTF."
    )
    parser.add_argument("font", help="Path to a TTF font file")
    parser.add_argument("--csv", metavar="FILE", help="Also write the table as CSV")
    args = parser.parse_args()

    font = TTFont(args.font)
    cmap = font.getBestCmap()
    glyph_set = font.getGlyphSet()
    hmtx = font["hmtx"]

    # References.
    ref_w = measure(glyph_set, hmtx, cmap, REF_WIDTH_CHAR)
    ref_sb = measure(glyph_set, hmtx, cmap, REF_SB_CHAR)
    if ref_w is None:
        parser.error(
            f"font has no '{REF_WIDTH_CHAR}' glyph to normalize widths against"
        )
    if ref_sb is None or ref_sb["lsb"] is None:
        parser.error(
            f"font has no usable '{REF_SB_CHAR}' glyph to normalize side bearings against"
        )

    o_adv = ref_w["advance"]
    o_rsb = ref_w["rsb"]
    o_lsb = ref_w["lsb"]
    o_w = o_adv - o_rsb - o_lsb
    l_lsb = ref_sb["lsb"]
    l_rsb = ref_sb["rsb"]

    units = font["head"].unitsPerEm
    print(f"Font: {args.font}  (unitsPerEm={units})")
    print(
        f"Refs: width vs '{REF_WIDTH_CHAR}' (adv={o_adv:.0f}); "
        f"side bearings vs '{REF_SB_CHAR}' (LSB={l_lsb:.0f}, RSB={l_rsb:.0f})\n"
    )

    header = ["char", "name", "adv", "LSB", "RSB", "w/o", "LSB/l", "RSB/l"]
    widths = [4, 22, 6, 6, 6, 6, 6, 6]

    def row(cells):
        return "  ".join(
            str(c).ljust(w) if i == 1 else str(c).rjust(w)
            for i, (c, w) in enumerate(zip(cells, widths))
        )

    print(row(header))
    print(row(["-" * w for w in widths]))

    csv_rows = []
    for group, chars in GROUPS.items():
        measured = [measure(glyph_set, hmtx, cmap, ch) for ch in chars]
        measured = [m for m in measured if m is not None]
        if not measured:
            continue
        print(f"\n{group}")
        for m in measured:
            name = unicodedata.name(m["char"], "")
            cells = [
                m["char"],
                name[:22],
                _fmt_num(m["advance"]),
                _fmt_num(m["lsb"]),
                _fmt_num(m["rsb"]),
                _fmt_ratio(_ratio(m["advance"] - m["lsb"] - m["rsb"] - s, o_w - s)),
                _fmt_ratio(_ratio(m["lsb"], l_lsb)),
                _fmt_ratio(_ratio(m["rsb"], l_rsb)),
            ]
            print(row(cells))
            csv_rows.append([group] + cells)

    if args.csv:
        with open(args.csv, "w", newline="") as fh:
            writer = csv.writer(fh)
            writer.writerow(["group"] + header)
            writer.writerows(csv_rows)
        print(f"\nWrote {len(csv_rows)} rows to {args.csv}")

    font.close()


if __name__ == "__main__":
    main(s=174)
