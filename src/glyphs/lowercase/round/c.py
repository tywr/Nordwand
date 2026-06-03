import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from draw.loop import draw_loop
from draw.rect import draw_rect
from draw.corner import draw_corner
from glyphs.lowercase.round import RoundLowercaseGlyph


class LowercaseCGlyph(RoundLowercaseGlyph):
    name = "lowercase_c"
    unicode = "0x63"
    opening1 = 0.33
    opening2 = 0.66
    width_ratio = 0.98
    thinning = 1
    top_offset = 0.00
    sbr = 0.46

    def draw(self, pen, dc):

        b = dc.body_bounds(
            width=self.width_ratio * dc.width + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            overshoot_bottom=True,
            overshoot_top=True,
        )
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
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
            hx,
            hy,
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
            hx,
            hy,
            orientation="bottom-left",
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.xmid,
            yc1,
            b.x2 + 10,
            yc2,
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
