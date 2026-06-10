from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class LowercaseVGlyph(Glyph):
    name = "lowercase_v"
    unicode = "0x76"
    width_ratio = 0.98
    bold_width_ratio = 1.06
    overlap = 0.5
    stroke_ratio = 0.97
    sbl = 0.4
    sbr = 0.4

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.15)
        ov = self.overlap * dc.stroke_x

        theta, delta = draw_parallelogramm(
            pen,
            sx,
            sx,
            b.xmid - ov,
            0,
            b.x2,
            b.y2,
        )
        draw_parallelogramm(
            pen,
            sx,
            sx,
            b.xmid + ov,
            0,
            b.x1,
            b.y2,
            direction="top-left",
        )
