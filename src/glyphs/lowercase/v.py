from math import tan, pi
from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect


class LowercaseVGlyph(Glyph):
    name = "lowercase_v"
    unicode = "0x76"
    width_ratio = 1
    overlap = 0.25
    stroke_ratio = 0.9
    sbl = 0.4
    sbr = 0.4

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width=self.width_ratio * dc.width + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        sx = self.stroke_ratio * dc.stroke_x
        ov = self.overlap * dc.stroke_x

        theta, delta = draw_parallelogramm(
            pen,
            sx,
            sx,
            b.xmid - ov,
            0,
            b.x2,
            b.y2,
        )
        draw_parallelogramm(
            pen,
            sx,
            sx,
            b.xmid + ov,
            0,
            b.x1,
            b.y2,
            direction="top-left",
        )
