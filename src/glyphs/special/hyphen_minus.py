from glyphs import Glyph
from draw.rect import draw_rect


class HyphenMinusGlyph(Glyph):
    name = "hyphen_minus"
    unicode = "0x2D"
    width_ratio = 0.68
    stroke_ratio = 0.9
    sbl = 0.84
    sbr = 0.84
    bold_width_ratio = 0.669
    bold_sbl = 1.051
    bold_sbr = 1.045

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        s = self.stroke_ratio * dc.stroke_x
        draw_rect(
            pen,
            b.x1,
            dc.math + s / 2,
            b.x2,
            dc.math - s / 2,
        )
