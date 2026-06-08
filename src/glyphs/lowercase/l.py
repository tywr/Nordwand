from glyphs import Glyph
from draw.rect import draw_rect


class LowercaseLGlyph(Glyph):
    name = "lowercase_l"
    unicode = "0x6C"
    width_ratio = 0
    sbl = 1
    sbr = 1

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

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        # Stem
        draw_rect(pen, b.xmid - dc.stroke_x / 2, 0, b.xmid + dc.stroke_x / 2, dc.ascent)
