import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class UppercaseWGlyph(UppercaseGlyph):
    name = "uppercase_w"
    unicode = "0x57"
    outer_branch_ratio = 0.265
    inner_height = 1
    overlap = 1
    width_ratio = 1.813
    bold_width_ratio = 1.905
    stroke_ratio = 1.1
    inner_stroke_ratio = 1
    lower_section_height = 1.5
    sbr = 0.523
    sbl = 0.523
    bold_sbl = 0.564
    bold_sbr = 0.558

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx = dc.stroke_x * self.stroke_ratio
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
