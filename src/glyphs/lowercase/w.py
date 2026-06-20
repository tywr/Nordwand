import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class LowercaseWGlyph(Glyph):
    name = "lowercase_w"
    unicode = "0x77"
    overlap = 1
    outer_branch_ratio = 0.27
    inner_height = 1
    width_ratio = 1.652
    bold_width_ratio = 1.833
    stroke_ratio = 1.05
    lower_section_height = 1.5
    sbl = 0.195
    sbr = 0.195
    bold_sbl = 0.127
    bold_sbr = 0.127

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.15)
        ov = self.overlap * sx
        xi1 = b.x1 + self.outer_branch_ratio * b.width
        xi2 = b.x2 - self.outer_branch_ratio * b.width
        yi = b.y1 + self.inner_height * b.height
        lsh = self.lower_section_height * dc.stroke_y

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        draw_parallelogramm(
            gpen,
            0,
            0,
            b.x1,
            b.y2,
            xi1 + ov / 2,
            b.y1,
            delta=sx,
            direction="bottom-right",
        )
        draw_parallelogramm(
            gpen,
            0,
            0,
            b.x2,
            b.y2,
            xi2 - ov / 2,
            b.y1,
            delta=sx,
            direction="bottom-left",
        )
        draw_parallelogramm(
            gpen,
            0,
            0,
            xi1 - ov / 2,
            b.y1,
            b.xmid + sx / 2,
            yi,
            delta=sx,
            direction="top-right",
        )
        draw_parallelogramm(
            gpen,
            0,
            0,
            xi2 + ov / 2,
            b.y1,
            b.xmid - sx / 2,
            yi,
            delta=sx,
            direction="top-left",
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[
                (b.x1 + sx, b.y2),
                (b.xmid - sx / 2, b.y2),
                (xi1, lsh),
            ],
        )
        draw_polygon(
            cut_glyph.getPen(),
            points=[
                (b.xmid + sx / 2, b.y2),
                (b.x2 - sx, b.y2),
                (xi2, lsh),
            ],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
