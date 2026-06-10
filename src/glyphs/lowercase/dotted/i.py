from draw.rect import draw_rect
from glyphs.lowercase.dotted import DottedLowercaseGlyph


class LowercaseIGlyph(DottedLowercaseGlyph):
    name = "lowercase_i"
    unicode = "0x69"
    cap = 0.5
    sbr = 0.97
    sbl = 0.97

    def window_width(self, dc):
        return dc.stroke_x + (self.sbr + self.sbl) * dc.side_bearing

    def body_bounds(self, dc):
        return dc.body_bounds(
            width=dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            height=self.height,
            number=self.number,
            uppercase=self.uppercase,
            overshoot_bottom=self.overshoot_bottom,
            overshoot_top=self.overshoot_top,
        )

    def draw_base(self, pen, dc):
        """Draw the letter without the dot (for use with accents)."""
        b = self.body_bounds(dc)
        # Stem
        draw_rect(
            pen, b.xmid - dc.stroke_x / 2, 0, b.xmid + dc.stroke_x / 2, dc.x_height
        )
