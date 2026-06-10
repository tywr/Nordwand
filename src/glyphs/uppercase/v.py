from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm


class UppercaseVGlyph(UppercaseGlyph):
    name = "uppercase_v"
    unicode = "0x56"
    stroke_x_ratio = 1.02
    width_ratio = 1.249
    bold_width_ratio = 1.343
    sbl = 0.401
    sbr = 0.401
    bold_sbl = 0.462
    bold_sbr = 0.455

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        ov = 0.5 * dc.stroke_x

        theta, delta = draw_parallelogramm(
            pen,
            sx,
            sy,
            b.xmid - ov,
            0,
            b.x2,
            b.y2,
        )
        draw_parallelogramm(
            pen,
            sx,
            sy,
            b.xmid + ov,
            0,
            b.x1,
            b.y2,
            direction="top-left",
        )
