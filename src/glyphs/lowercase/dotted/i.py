from draw.rect import draw_rect
from glyphs.lowercase.dotted import DottedLowercaseGlyph


class LowercaseIGlyph(DottedLowercaseGlyph):
    name = "lowercase_i"
    unicode = "0x69"
    offset = 16
    width_ratio = 0
    cap = 0.5
    rl_ratio = 0.5
    sbr = 1
    sbl = 1

    def draw_base(self, pen, dc):
        """Draw the letter without the dot (for use with accents)."""
        b = dc.body_bounds(
            width=self.width_ratio * dc.width + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        # Stem
        draw_rect(
            pen, b.xmid - dc.stroke_x / 2, 0, b.xmid + dc.stroke_x / 2, dc.x_height
        )
