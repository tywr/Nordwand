from draw.rect import draw_rect
from glyphs.lowercase.dotted import DottedLowercaseGlyph


class LowercaseIGlyph(DottedLowercaseGlyph):
    name = "lowercase_i"
    unicode = "0x69"
    width_ratio = 0
    cap = 0.5
    rl_ratio = 0.5
    sbr = 0.96
    sbl = 0.96

    def draw_base(self, pen, dc):
        """Draw the letter without the dot (for use with accents)."""
        b = self.body_bounds(dc)
        # Stem
        draw_rect(
            pen, b.xmid - dc.stroke_x / 2, 0, b.xmid + dc.stroke_x / 2, dc.x_height
        )
