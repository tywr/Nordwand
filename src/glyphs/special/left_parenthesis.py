from glyphs import Glyph
from draw.loop import draw_loop


class LeftParenthesisGlyph(Glyph):
    name = "left_parenthesis"
    unicode = "0x28"
    stroke_x_ratio = 1.1
    width_ratio = 0.358
    sbl = 0.841
    sbr = 0.634
    bold_width_ratio = 0.439
    bold_sbl = 0.789
    bold_sbr = 0.606

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
