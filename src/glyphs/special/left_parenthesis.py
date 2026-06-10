from glyphs import Glyph
from draw.loop import draw_loop


class LeftParenthesisGlyph(Glyph):
    name = "left_parenthesis"
    unicode = "0x28"
    width_ratio = 0.4
    stroke_x_ratio = 1.1
    bold_width_ratio = 0.569
    bold_sbl = 1.429
    bold_sbr = 0.577

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = self.stroke_x_ratio * dc.stroke_x, dc.stroke_y
        ymid = dc.parenthesis
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            ymid - dc.parenthesis_length / 2,
            b.x1 + 2 * (b.x2 - b.x1),
            ymid + dc.parenthesis_length / 2,
            b.hx * 2,
            b.hy * dc.parenthesis_length / b.height,
            cut="right"
        )
