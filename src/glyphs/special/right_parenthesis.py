from glyphs import Glyph
from draw.loop import draw_loop


class RightParenthesisGlyph(Glyph):
    name = "right_parenthesis"
    unicode = "0x29"
    stroke_x_ratio = 1.1
    width_ratio = 0.360
    sbl = 0.634
    sbr = 0.841
    bold_width_ratio = 0.398
    bold_sbl = 0.606
    bold_sbr = 0.789

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = self.stroke_x_ratio * dc.stroke_x, dc.stroke_y
        ymid = dc.parenthesis
        draw_loop(
            pen,
            sx,
            sy,
            b.x2 - 2 * (b.x2 - b.x1),
            ymid - dc.parenthesis_length / 2,
            b.x2,
            ymid + dc.parenthesis_length / 2,
            b.hx * 2,
            b.hy * dc.parenthesis_length / b.height,
            cut="left",
        )
