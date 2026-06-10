from glyphs import Glyph
from draw.rect import draw_rect


class PlusSignGlyph(Glyph):
    name = "plus_sign"
    unicode = "0x2B"
    width_ratio = 1
    stroke_ratio = 0.88
    height = "cap"
    bold_width_ratio = 1.136
    bold_sbl = 0.795
    bold_sbr = 0.788

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        s = dc.stroke_x * self.stroke_ratio

        draw_rect(pen, b.x1, dc.math - s / 2, b.x2, dc.math + s / 2)
        draw_rect(pen, b.xmid - s / 2, dc.math - b.width / 2, b.xmid + s / 2, dc.math + b.width / 2)
