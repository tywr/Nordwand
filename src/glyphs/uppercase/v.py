import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class UppercaseVGlyph(UppercaseGlyph):
    name = "uppercase_v"
    unicode = "0x56"
    stroke_x_ratio = 1.1
    width_ratio = 1.318
    bold_width_ratio = 1.437
    lower_section_height = 1.5
    sbl = 0.073
    sbr = 0.073
    bold_sbl = -0.056
    bold_sbr = -0.056

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx = self.stroke_x_ratio * dc.stroke_x
        ov = 0.5 * dc.stroke_x
        lsh = self.lower_section_height * dc.stroke_y

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        theta, delta = draw_parallelogramm(
            gpen,
            sx,
            sx,
            b.xmid - ov,
            0,
            b.x2,
            b.y2,
            delta=sx
        )
        draw_parallelogramm(
            gpen,
            sx,
            sx,
            b.xmid + ov,
            0,
            b.x1,
            b.y2,
            direction="top-left",
            delta=sx
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[(b.x1 + sx, b.y2), (b.x2 - sx, b.y2), (b.xmid, b.y1 + lsh)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
