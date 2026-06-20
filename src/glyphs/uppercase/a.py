import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from math import cos
from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect
from draw.polygon import draw_polygon


class UppercaseAGlyph(UppercaseGlyph):
    name = "uppercase_a"
    unicode = "0x41"
    bar_height = 0.39
    overlap = 0.5
    stroke_x_ratio = 1.1
    width_ratio = 1.412
    bold_width_ratio = 1.401
    higher_section_height = 1.5
    sbl = 0.061
    sbr = 0.061
    bold_sbl = -0.070
    bold_sbr = -0.070

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        half_width = b.width / 2 - sx / 2
        ov = 0.5 * dc.stroke_x
        hb = self.bar_height * b.height
        hsh = self.higher_section_height * dc.stroke_y

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        # Left branch
        draw_parallelogramm(
            gpen, sx, sx, b.x2, b.y1, b.xmid - ov, b.y2, direction="top-left", delta=sx
        )
        # Right branch
        theta, delta = draw_parallelogramm(
            gpen, sx, sx, b.x1, b.y1, b.xmid + ov, b.y2, delta=sx
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_polygon(
            cut_glyph.getPen(),
            points=[(b.x1 + sx, b.y1), (b.x2 - sx, b.y1), (b.xmid, b.y2 - hsh)],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)

        # Crossbar
        draw_rect(
            pen,
            b.xmid - (hb - sy) * cos(theta),
            hb - sy,
            b.xmid + (hb - sy) * cos(theta),
            hb,
        )
