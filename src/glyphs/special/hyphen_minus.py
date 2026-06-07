from glyphs import Glyph
from draw.rect import draw_rect


class HyphenMinusGlyph(Glyph):
    name = "hyphen_minus"
    unicode = "0x2D"
    width_ratio = 0.88
    stroke_ratio = 0.8

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
