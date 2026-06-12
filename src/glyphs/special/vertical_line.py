from glyphs import Glyph
from draw.rect import draw_rect


class VerticalLineGlyph(Glyph):
    name = "vertical_line"
    unicode = "0x7C"
    width_ratio = 0.00
    sbl = 1.070
    sbr = 1.070
    bold_width_ratio = 0.0
    bold_sbl = 1.070
    bold_sbr = 1.070

    def window_width(self, dc):
        return dc.stroke_x + (self.sbr + self.sbl) * dc.side_bearing

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

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        draw_rect(pen, b.xmid - dc.stroke_x / 2, dc.descent, b.xmid + dc.stroke_x / 2, dc.ascent)
