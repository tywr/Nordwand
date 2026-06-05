from math import tan, pi
from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect


class UppercaseVGlyph(UppercaseGlyph):
    name = "uppercase_v"
    unicode = "0x56"
    overlap = 0.5
    stroke_x_ratio = 1.02
    width_ratio = 1.30
    sbl = 0.4
    sbr = 0.4

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            uppercase=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        ov = self.overlap * sx

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
