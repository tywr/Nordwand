from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm


class UppercaseWGlyph(UppercaseGlyph):
    name = "uppercase_w"
    unicode = "0x57"
    outer_branch_ratio = 0.26
    inner_height = 1
    width_ratio = 1.812
    stroke_ratio = 1.1
    inner_stroke_ratio = 1
    sbr = 0.53
    sbl = 0.53

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        ov = 1.3 * max(dc.stroke_x - 94, 0)
        tsx = dc.stroke_x * self.stroke_ratio
        sx = max(0, 0.7 * (tsx - 90)) + min(90, tsx)
        xi1 = b.x1 + self.outer_branch_ratio * b.width
        xi2 = b.x2 - self.outer_branch_ratio * b.width
        yi = b.y1 + self.inner_height * b.height

        draw_parallelogramm(
            pen,
            0,
            0,
            b.x1,
            b.y2,
            xi1 + sx / 2 - ov / 2,
            b.y1,
            delta=sx,
            direction="bottom-right",
        )
        draw_parallelogramm(
            pen,
            0,
            0,
            b.x2,
            b.y2,
            xi2 - sx / 2 + ov / 2,
            b.y1,
            delta=sx,
            direction="bottom-left",
        )
        draw_parallelogramm(
            pen,
            0,
            0,
            xi1 - sx / 2 + ov / 2,
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
            xi2 + sx / 2 - ov / 2,
            b.y1,
            b.xmid - sx / 2,
            yi,
            delta=sx,
            direction="top-left",
        )
