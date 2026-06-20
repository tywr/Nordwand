from glyphs import Glyph
from draw.rect import draw_rect


class EqualsSignGlyph(Glyph):
    name = "equals_sign"
    unicode = "0x3D"
    gap = 0.5
    stroke_ratio = 0.92
    width_ratio = 1.024
    sbl = 1.000
    sbr = 1.000
    bold_width_ratio = 0.958
    bold_sbl = 0.986
    bold_sbr = 0.986

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        s = dc.stroke_x * self.stroke_ratio
        g = self.gap * b.height
        draw_rect(
            pen,
            b.x1,
            dc.math + g / 2 - s / 2,
            b.x2,
            dc.math + g / 2 + s / 2,
        )
        draw_rect(
            pen,
            b.x1,
            dc.math - g / 2 - s / 2,
            b.x2,
            dc.math - g / 2 + s / 2,
        )
