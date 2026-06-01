from math import tan
from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect


class UppercaseXGlyph(UppercaseGlyph):
    name = "uppercase_x"
    unicode = "0x58"
    width_ratio = 1.4
    stroke_x_ratio = 1.08

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        draw_parallelogramm(pen, sx, sy, b.x1, b.y1, b.x2, b.y2)
        theta, delta = draw_parallelogramm(
            pen, sx, sy, b.x2, b.y1, b.x1, b.y2, direction="top-left"
        )
