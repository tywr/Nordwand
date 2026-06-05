from glyphs import Glyph
from draw.loop import draw_loop


class RightParenthesisGlyph(Glyph):
    name = "right_parenthesis"
    unicode = "0x29"
    width_ratio = 0.4
    stroke_x_ratio = 1.1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="x_height",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
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
