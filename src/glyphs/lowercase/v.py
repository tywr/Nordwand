from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class LowercaseVGlyph(Glyph):
    name = "lowercase_v"
    unicode = "0x76"
    width_ratio = 0.98
    overlap = 0.33
    stroke_ratio = 1
    sbl = 0.4
    sbr = 0.4

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width=self.width_ratio * dc.width + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        sx = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.15)
        ov = self.overlap * dc.stroke_x - 0.12 * max(dc.stroke_x - 94, 0)

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
