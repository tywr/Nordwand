#!/usr/bin/env python3
"""Render a lorem-ipsum specimen as a PNG to display the font.

Usage: python -m scripts.samples [font.ttf] [-o OUTPUT_DIR]
"""

import argparse
import os

from PIL import Image, ImageDraw, ImageFont


# Dark specimen palette.
BG = "#121212"
FG = "#cccccc"

FONT_SIZE = 42
IMAGE_PAD = 96
LINE_LEADING = int(FONT_SIZE * 1.55)
PARA_GAP = int(FONT_SIZE * 0.8)
TEXT_WIDTH = 1500  # text column width in pixels


LOREM = """\
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo.
"""


def wrap_to_width(text, font, max_width):
    """Word-wrap `text` to `max_width` pixels, keeping blank lines between
    paragraphs. Measures real advances, so it works for proportional fonts."""
    lines = []
    paragraphs = [p for p in text.split("\n\n")]
    for i, para in enumerate(paragraphs):
        if i > 0:
            lines.append("")  # paragraph break
        current = ""
        for word in para.split():
            trial = f"{current} {word}".strip()
            if not current or font.getlength(trial) <= max_width:
                current = trial
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def render_lorem(output, font_path, font_size=FONT_SIZE):
    font = ImageFont.truetype(font_path, font_size)
    lines = wrap_to_width(LOREM, font, TEXT_WIDTH)

    img_w = TEXT_WIDTH + 2 * IMAGE_PAD
    img_h = 2 * IMAGE_PAD
    for line in lines:
        img_h += PARA_GAP if line == "" else LINE_LEADING

    img = Image.new("RGB", (img_w, img_h), BG)
    draw = ImageDraw.Draw(img)

    y = IMAGE_PAD
    for line in lines:
        if line == "":
            y += PARA_GAP
            continue
        # liga/calt so the font's ligatures/contextual alternates fire.
        draw.text((IMAGE_PAD, y), line, font=font, fill=FG, features=["liga", "calt"])
        y += LINE_LEADING

    os.makedirs(os.path.dirname(output), exist_ok=True)
    img.save(output)
    print(f"Saved {output} ({img.width}x{img.height})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a lorem-ipsum font specimen PNG")
    parser.add_argument(
        "font",
        nargs="?",
        default="fonts/ttf/Nordwand-Regular.ttf",
        help="Path to font file",
    )
    parser.add_argument(
        "-o", "--output-dir", default="assets/samples", help="Output directory"
    )
    parser.add_argument("--size", type=int, default=FONT_SIZE, help="Font size in px")
    args = parser.parse_args()

    render_lorem(
        os.path.join(args.output_dir, "lorem.png"),
        args.font,
        font_size=args.size,
    )
