from math import tan
from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class LowercaseYGlyph(Glyph):
    name = "lowercase_y"
    unicode = "0x79"
    offset = 0
    width_ratio = 1.15
    overlap = 0.285
    dent_ratio = 0.1
    sbl = 0.65
    sbr = 0.65

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width=dc.width * self.width_ratio + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        dent_height = self.dent_ratio * b.height
        ov = self.overlap * dc.stroke_x

        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid + ov,
            dent_height,
            b.x1,
            b.y2,
            direction="top-left",
        )
        theta, delta = draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid - ov,
            dent_height,
            b.x2,
            b.y2,
        )
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid - ov + delta,
            dent_height,
            b.xmid - ov - (abs(dc.descent) + dent_height) / tan(theta),
            dc.descent,
            direction="bottom-left",
        )
