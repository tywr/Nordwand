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
    mid_height = 0.52
    width_ratio = 0.89
    taper = 0.6
    sbl = 0.58
    sbr = 0.9

    left_cap_hx_ratio = 1.25
    left_cap_hy_ratio = 1.32
    cap_hx_ratio = 1.2
    cap_hy_ratio = 1
    cap_height = 0.74
    cap_offset = 0.015
    thinning = 1
    upper_bowl_mid = 0.53
    cap_stroke_x_ratio = 1.01
    cap_stroke_y_ratio = 1.00
    ending_thickness = 0.7

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width=dc.width * self.width_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            overshoot_top=True,
            overshoot_bottom=True,
        )
        sx = dc.stroke_x
        csx, csy = (
            self.cap_stroke_x_ratio * dc.stroke_x,
            self.cap_stroke_y_ratio * dc.stroke_y,
        )
        dx = csx - dc.stroke_x
        ry = (self.mid_height * b.height + dc.stroke_alt / 2) / b.height
        ymid = b.y1 + self.mid_height * b.height
        xmu = b.x1 + self.upper_bowl_mid * b.width
        yl = ymid + dc.stroke_alt / 2
        hx, hy = b.hx, b.hy * ry
        ycut = b.y1 + self.cap_height * b.height
        xc = b.x1 + self.cap_offset * b.width
        chx = self.cap_hx_ratio * b.hx
        lchx = self.left_cap_hx_ratio * b.hx
        lchy = self.left_cap_hy_ratio * b.hy

        # Lower half half of the bowl
        draw_arch(
            pen,
            csx,
            csy,
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
            csx,
            dc.stroke_alt,
            b.x1,
            (b.y1 + yl) / 2,
            xmu,
            yl,
            hx,
            hy,
            orientation="top-right",
        )
        draw_rect(
            pen,
            xmu,
            yl - dc.stroke_alt,
            b.x2 - 0.5 * dc.stroke_x,
            yl,
        )

        # Cap
        xmid = (xc + b.x2) / 2
        draw_corner(
            pen, sx, csy, b.x2, b.ymid, xmid, b.y2, lchx, lchy, orientation="top-left"
        )

        loop_glyph = ufoLib2.objects.Glyph()
        draw_corner(
            loop_glyph.getPen(),
            csx * self.thinning,
            csy,
            xc,
            b.ymid,
            xmid,
            b.y2,
            chx,
            b.hy,
            orientation="top-right",
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(cut_glyph.getPen(), b.x1, b.ymid, b.xmid, ycut)
        result = BooleanGlyph(loop_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        # Stem
        draw_rect(
            pen,
            b.x2 - sx,
            0,
            b.x2,
            b.ymid,
        )
