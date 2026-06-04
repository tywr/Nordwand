from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class LowercaseWGlyph(Glyph):
    name = "lowercase_w"
    unicode = "0x77"
    overlap = 0.25
    outer_branch_ratio = 0.25
    inner_height = 1
    width_ratio = 1.6
    stroke_ratio = 0.88
    inner_stroke_ratio = 1
    sbl = 0.2
    sbr = 0.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width=self.width_ratio * dc.width + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        sx = dc.stroke_x * self.stroke_ratio
        ov = self.overlap * dc.stroke_x
        # sx = max(0, 0.7 * (tsx - 90)) + min(90, tsx)
        isx = sx * self.inner_stroke_ratio
        xi1 = b.x1 + self.outer_branch_ratio * b.width + sx / 2
        xi2 = b.x2 - self.outer_branch_ratio * b.width - sx / 2
        yi = b.y1 + self.inner_height * b.height

        draw_parallelogramm(
            pen,
            0,
            0,
            b.x1,
            b.y2,
            xi1 - ov,
            b.y1,
            delta=sx,
            direction="bottom-right",
        )
        draw_parallelogramm(
            pen, 0, 0, b.x2, b.y2, xi2 + ov, b.y1, delta=sx, direction="bottom-left"
        )
        draw_parallelogramm(
            pen,
            0,
            0,
            xi1 - ov - sx / 2,
            b.y1,
            b.xmid + sx / 2,
            yi,
            delta=sx,
            direction="top-right",
        )
        draw_parallelogramm(
            pen,
            0,
            0,
            xi2 + ov + sx / 2,
            b.y1,
            b.xmid - sx / 2,
            yi,
            delta=sx,
            direction="top-left",
        )
