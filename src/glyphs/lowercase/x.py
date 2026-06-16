from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class LowercaseXGlyph(Glyph):
    name = "lowercase_x"
    unicode = "0x78"
    stroke_ratio = 1.05
    width_ratio = 0.933
    bold_width_ratio = 1.070
    sbl = 0.43
    sbr = 0.43
    bold_sbl = 0.404
    bold_sbr = 0.404

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.15)
        draw_parallelogramm(
            pen, dc.stroke_x, dc.stroke_y, b.x1, b.y1, b.x2, b.y2, delta=sx
        )
        theta, delta = draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2,
            b.y1,
            b.x1,
            b.y2,
            direction="top-left",
            delta=sx,
        )
