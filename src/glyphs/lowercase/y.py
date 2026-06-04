from math import tan
from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class LowercaseYGlyph(Glyph):
    name = "lowercase_y"
    unicode = "0x79"
    width_ratio = 1.0
    overlap = 0.25
    dent_ratio = 0
    stroke_ratio = 0.9
    sbl = 0.5
    sbr = 0.5

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width=dc.width * self.width_ratio + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        sx = self.stroke_ratio * dc.stroke_x
        dent_height = self.dent_ratio * b.height
        ov = self.overlap * dc.stroke_x

        draw_parallelogramm(
            pen,
            sx,
            sx,
            b.xmid + ov,
            dent_height,
            b.x1,
            b.y2,
            direction="top-left",
        )
        theta, delta = draw_parallelogramm(
            pen,
            sx,
            sx,
            b.xmid - ov,
            dent_height,
            b.x2,
            b.y2,
        )
        draw_parallelogramm(
            pen,
            sx,
            sx,
            b.xmid - ov + delta,
            dent_height,
            b.xmid - ov - (abs(dc.descent) + dent_height) / tan(theta),
            dc.descent,
            direction="bottom-left",
        )
