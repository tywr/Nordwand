from draw.rect import draw_rect
from glyphs.lowercase.dotted import DottedLowercaseGlyph


class LowercaseIGlyph(DottedLowercaseGlyph):
    name = "lowercase_i"
    unicode = "0x69"
    bold_width_ratio = 0.306
    width_ratio = 0.197
    cap = 0.5
    sbr = 1
    sbl = 1
    bold_sbl = 1
    bold_sbr = 1

    def window_width(self, dc):
        return (
            dc.stroke_x
            + (self.adjusted_sbr(dc) + self.adjusted_sbl(dc)) * dc.side_bearing
        )

    def body_bounds(self, dc):
        return dc.body_bounds(
            width=dc.stroke_x,
            side_bearing_right=self.adjusted_sbr(dc) * dc.side_bearing,
            side_bearing_left=self.adjusted_sbl(dc) * dc.side_bearing,
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
