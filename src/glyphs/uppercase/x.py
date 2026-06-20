from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm


class UppercaseXGlyph(UppercaseGlyph):
    name = "uppercase_x"
    unicode = "0x58"
    width_ratio = 1.316
    bold_width_ratio = 1.505
    stroke_x_ratio = 1.08
    sbr = 0.085
    sbl = 0.085
    bold_sbl = -0.056
    bold_sbr = -0.056

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        draw_parallelogramm(pen, sx, sy, b.x1, b.y1, b.x2, b.y2)
        theta, delta = draw_parallelogramm(
            pen, sx, sy, b.x2, b.y1, b.x1, b.y2, direction="top-left"
        )
