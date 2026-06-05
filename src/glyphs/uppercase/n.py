from math import tan, pi
from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm_vertical
from utils.pens import NullPen


class UppercaseNGlyph(UppercaseGlyph):
    name = "uppercase_n"
    unicode = "0x4E"
    middle_stroke_ratio = 0.9
    overlap = 0.3
    width_ratio = 1.19
    sbl = 1.07
    sbr = 1.07

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            uppercase=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        # Vertical stems
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        draw_rect(pen, b.x2 - sx, b.y1, b.x2, b.y2)

        # Diagonal
        theta, delta = draw_parallelogramm_vertical(
            pen,
            sx * self.middle_stroke_ratio,
            sy * self.middle_stroke_ratio,
            b.x2 - sx,
            b.y1,
            b.x1 + sx,
            b.y2,
            direction="top-left",
        )
