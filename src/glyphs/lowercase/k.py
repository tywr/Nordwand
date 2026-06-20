from glyphs import Glyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class LowercaseKGlyph(Glyph):
    name = "lowercase_k"
    unicode = "0x6B"
    width_ratio = 0.905
    bold_width_ratio = 0.984
    mid_ratio = 0.57
    upper_branch_offset = 0.04
    branch_stroke_ratio = 1.3
    branch_overlap = 0.8
    sbl = 1.000
    sbr = 0.122
    bold_sbl = 1.000
    bold_sbr = 0.141

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
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
