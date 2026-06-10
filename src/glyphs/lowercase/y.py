import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm
from draw.polygon import draw_polygon


class LowercaseYGlyph(Glyph):
    name = "lowercase_y"
    unicode = "0x79"
    width_ratio = 0.982
    bold_width_ratio = 1.09
    overlap = 0.5
    stroke_ratio = 1.1
    lower_section_height = 1.3
    sbl = 0.395
    sbr = 0.395

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx = self.stroke_ratio * dc.stroke_x
        ov = self.overlap * sx
        lsh = self.lower_section_height * dc.stroke_y

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        draw_parallelogramm(
            gpen,
            sx,
            sx,
            b.xmid + ov,
            b.y1,
            b.x1,
            b.y2,
            direction="top-left",
            delta=sx,
        )
        theta, delta = draw_parallelogramm(
            gpen,
            sx,
            sx,
            b.x2,
            b.y2,
            b.xmid - ov,
            b.y1,
            delta=sx,
            direction="bottom-left",
        )
        # Prolong the right v-stroke straight into the descender: share its
        # bottom edge and continue at the same slant (same delta, same slope).
        w2 = b.x2 - (b.xmid - ov)
        h2 = b.y2 - b.y1
        dx_tail = -(w2 - delta) * abs(dc.descent) / h2
        draw_parallelogramm(
            gpen,
            sx,
            sx,
            b.xmid - ov + delta,
            b.y1,
            b.xmid - ov + dx_tail,
            dc.descent,
            direction="bottom-left",
            delta=delta,
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[(b.x1 + sx, b.y2), (b.x2 - sx, b.y2), (b.xmid, b.y1 + lsh)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
