import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class LowercaseVGlyph(Glyph):
    name = "lowercase_v"
    unicode = "0x76"
    width_ratio = 0.98
    bold_width_ratio = 1.099
    overlap = 0.5
    stroke_ratio = 1.05
    lower_section_height = 1.3
    sbl = 0.4
    sbr = 0.4
    bold_sbl = 0.327
    bold_sbr = 0.327

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.15)
        ov = self.overlap * dc.stroke_x
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
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[(b.x1 + sx, b.y2), (b.x2 - sx, b.y2), (b.xmid, b.y1 + lsh)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
