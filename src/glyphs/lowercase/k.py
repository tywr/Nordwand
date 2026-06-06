from glyphs import Glyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class LowercaseKGlyph(Glyph):
    name = "lowercase_k"
    unicode = "0x6B"
    width_ratio = 0.85
    mid_ratio = 0.52
    upper_branch_offset = 0.03
    branch_stroke_ratio = 1.3
    branch_overlap = 0.8
    sbl = 1
    sbr = 0.43

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width=dc.width * self.width_ratio
            + 0.5 * self.branch_stroke_ratio * dc.stroke_x
            + 0.5 * dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        xb = b.x1 + self.branch_overlap * dc.stroke_x
        sx = self.diag_stroke_dampening(self.branch_stroke_ratio, dc.stroke_x, coef=0.15)
        xtop = b.x2 - self.upper_branch_offset * b.width
        ymid = b.y1 + self.mid_ratio * b.height

        # Left ascender stem
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, dc.ascent)

        # Lower branch
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xb,
            ymid,
            b.x2,
            b.y1,
            direction="bottom-right",
            delta=sx,
        )

        # Upper branch
        theta, delta = draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xb,
            ymid,
            xtop,
            b.y2,
            delta=sx,
        )
