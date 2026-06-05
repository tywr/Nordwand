from glyphs import Glyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class LowercaseZGlyph(Glyph):
    name = "lowercase_z"
    unicode = "0x7A"
    diag_stroke_ratio = 0.96
    width_ratio = 0.8
    right_offset = 0.04
    left_offset = 0.025
    sbl = 0.8
    sbr = 0.8

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        dsx = self.diag_stroke_ratio * dc.stroke_x
        dsy = self.diag_stroke_ratio * dc.stroke_y

        xl = b.x1 + self.left_offset * b.width
        xr = b.x2 - self.right_offset * b.width

        # Top and bottom bars
        draw_rect(pen, xl, dc.x_height - dc.stroke_y, xr, dc.x_height)
        draw_rect(pen, b.x1, 0, b.x2, dc.stroke_y)

        # Diagonal stroke
        theta, delta = draw_parallelogramm(
            pen,
            dsx,
            dsy,
            b.x1,
            b.y1 + dc.stroke_y,
            xr,
            b.y2 - dc.stroke_y,
        )
