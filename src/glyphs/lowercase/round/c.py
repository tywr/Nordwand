import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from draw.loop import draw_loop
from draw.rect import draw_rect
from draw.corner import draw_corner
from glyphs.lowercase.round import RoundLowercaseGlyph


class LowercaseCGlyph(RoundLowercaseGlyph):
    name = "lowercase_c"
    unicode = "0x63"
    opening1 = 0.31
    opening2 = 0.685
    width_ratio = 0.94
    bold_width_ratio = 0.922
    thinning = 0.9
    top_offset = 0.00
    stroke_x_ratio = 1.03
    sbl = 0.549
    sbr = 0.300
    right_hx_ratio = 1.2
    right_hy_ratio = 1
    bold_sbl = 0.521
    bold_sbr = 0.324

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        ec = self.extra_cut(dc)
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        rhx, rhy = self.right_hx_ratio * b.hx, self.right_hy_ratio * b.hy
        yc1 = b.y1 + b.height * self.opening1
        yc2 = b.y1 + b.height * self.opening2
        xt = b.x2 - self.top_offset * b.width

        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, b.y2, hx, hy, cut="right")

        glyph = ufoLib2.objects.Glyph()
        draw_corner(
            glyph.getPen(),
            sx * self.thinning,
            sy,
            xt,
            b.ymid,
            b.xmid,
            b.y2,
            rhx,
            rhy,
            orientation="top-left",
        )
        draw_corner(
            glyph.getPen(),
            sx * self.thinning,
            sy,
            b.x2,
            b.ymid,
            b.xmid,
            b.y1,
            rhx,
            rhy,
            orientation="bottom-left",
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.xmid,
            yc1 + ec,
            b.x2 + 10,
            yc2 - ec,
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
