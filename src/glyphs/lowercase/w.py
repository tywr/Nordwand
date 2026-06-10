from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class LowercaseWGlyph(Glyph):
    name = "lowercase_w"
    unicode = "0x77"
    overlap = 0.125
    outer_branch_ratio = 0.27
    inner_height = 1
    width_ratio = 1.46
    bold_width_ratio = 1.59
    stroke_ratio = 0.94
    sbl = 0.4
    sbr = 0.4

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.15)
        ov = self.overlap * dc.stroke_x
        xi1 = b.x1 + self.outer_branch_ratio * b.width
        xi2 = b.x2 - self.outer_branch_ratio * b.width
        yi = b.y1 + self.inner_height * b.height

        draw_parallelogramm(
            pen,
            0,
            0,
            b.x1,
            b.y2,
            xi1 - ov / 2 + sx / 2,
            b.y1,
            delta=sx,
            direction="bottom-right",
        )
        draw_parallelogramm(
            pen, 0, 0, b.x2, b.y2, xi2 + ov / 2 - sx / 2, b.y1, delta=sx, direction="bottom-left"
        )
        draw_parallelogramm(
            pen,
            0,
            0,
            xi1 + ov / 2 - sx / 2,
            b.y1,
            b.xmid + sx / 2,
            yi,
            delta=sx,
            direction="top-right",
        )
        draw_parallelogramm(
            pen,
            0,
            0,
            xi2 - ov / 2 + sx / 2,
            b.y1,
            b.xmid - sx / 2,
            yi,
            delta=sx,
            direction="top-left",
        )
