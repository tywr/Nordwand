import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.arch import draw_arch
from draw.corner import draw_corner
from draw.rect import draw_rect


class LowercaseAGlyph(Glyph):
    name = "lowercase_a"
    unicode = "0x61"
    accent_x_offset = 16
    mid_height = 0.525
    width_ratio = 0.881
    bold_width_ratio = 0.988
    taper = 0.4
    sbl = 0.570
    sbr = 0.907
    bold_sbl = 0.558
    bold_sbr = 0.897

    bot_hx_ratio = 1.2
    bot_hy_ratio = 0.9
    left_cap_hx_ratio = 1.05
    left_cap_hy_ratio = 0.65
    cap_mid_offset = 0.028
    cap_hx_ratio = 1.27
    cap_hy_ratio = 1.1
    cap_x_stroke_ratio = 1.01
    cap_y_stroke_ratio = 1.06
    cap_start_height = 0.68
    cap_height = 0.74
    cap_offset = 0.01
    thinning = 0.9
    upper_bowl_mid = 0.56
    ending_thickness = 0.7
    overshoot_top = True
    overshoot_bottom = True

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        ec = self.extra_cut(dc)
        sx, sy = dc.stroke_x, dc.stroke_y
        csx, csy = (
            dc.stroke_x * self.cap_x_stroke_ratio,
            dc.stroke_y * self.cap_y_stroke_ratio,
        )
        dx = sx - dc.stroke_x
        ry = (self.mid_height * b.height + dc.stroke_alt / 2) / b.height
        ymid = b.y1 + self.mid_height * b.height
        xmc = b.xmid + self.cap_mid_offset * b.width
        xmu = b.x1 + self.upper_bowl_mid * b.width
        ycap = b.y1 + self.cap_start_height * b.height
        yl = ymid + dc.stroke_alt / 2
        hx, hy = b.hx, b.hy * ry
        bhx, bhy = self.bot_hx_ratio * b.hx, self.bot_hy_ratio * b.hy
        ycut = b.y1 + self.cap_height * b.height
        xc = b.x1 + self.cap_offset * b.width
        chx, chy = self.cap_hx_ratio * b.hx, self.cap_hy_ratio * b.hy
        lchx = self.left_cap_hx_ratio * b.hx
        lchy = self.left_cap_hy_ratio * b.hy

        # Lower half half of the bowl
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2 + dx,
            yl,
            hx,
            hy,
            taper=self.taper * dc.taper,
            side="right",
            cut="top",
        )

        # Upper half of the bowl
        draw_corner(
            pen,
            sx,
            dc.stroke_alt,
            b.x1,
            (b.y1 + yl) / 2,
            b.x2 - sx,
            yl,
            bhx,
            bhy,
            orientation="top-right",
        )
        # draw_rect(
        #     pen,
        #     xmu,
        #     yl - dc.stroke_alt,
        #     b.x2 - 0.5 * dc.stroke_x,
        #     yl,
        # )

        # Cap
        draw_corner(
            pen, sx, csy, b.x2, ycap, xmc, b.y2, lchx, lchy, orientation="top-left"
        )

        loop_glyph = ufoLib2.objects.Glyph()
        draw_corner(
            loop_glyph.getPen(),
            csx * self.thinning,
            csy,
            xc,
            b.ymid,
            xmc,
            b.y2,
            chx,
            chy,
            orientation="top-right",
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(cut_glyph.getPen(), b.x1, b.ymid, b.xmid, ycut - ec)
        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        # Stem
        draw_rect(
            pen,
            b.x2 - sx,
            0,
            b.x2,
            ycap,
        )
