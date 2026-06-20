import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.loop import draw_loop
from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.corner import draw_corner
from draw.square_corner import draw_square_corner


class CommercialAtGlyph(Glyph):
    name = "commercial_at"
    unicode = "0x40"
    sbl = 0.610
    sbr = 0.598
    taper = 0.5
    width_ratio = 1.793
    y1_ratio = 0.2
    inner_ratio_x = 0.5
    inner_ratio_y = 0.55
    angle_hx_ratio = 0.4
    angle_hy_ratio = 0.55
    ending_thickness = 0.8
    height = "cap"
    overshoot_top = True
    bold_width_ratio = 1.865
    bold_sbl = 0.563
    bold_sbr = 0.535

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        y1 = b.y1 - self.y1_ratio * b.height
        ymid = (y1 + b.y2) / 2
        wi, hi = self.inner_ratio_x * b.width, self.inner_ratio_y * b.height
        xi1, xi2 = b.xmid - wi / 2, b.xmid + wi / 2
        yi1, yi2 = ymid - hi / 2, ymid + hi / 2
        ahx, ahy = self.angle_hx_ratio * b.hx, self.angle_hy_ratio * b.hy

        draw_arch(
            pen,
            dc.stroke_x,
            dc.stroke_alt,
            xi1,
            yi1,
            xi2,
            yi2,
            b.hx * self.inner_ratio_x,
            b.hy * self.inner_ratio_y,
            side="right",
            taper=self.taper * dc.taper,
        )

        draw_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xi2 - dc.stroke_x,
            yi1,
            b.x2,
            yi2,
            hx=ahx,
            hy=ahy,
            cut="top",
        )
        draw_rect(pen, xi2 - dc.stroke_x, (yi1 + b.ymid) / 2, xi2, yi2)
        # draw_rect(pen, b.x2 - dc.stroke_x, (yi1 + b.ymid) / 2, b.x2, b.ymid)

        draw_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2,
            ymid,
            b.xmid,
            b.y2,
            b.hx,
            b.hy,
            orientation="top-left",
        )

        draw_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            y1,
            b.x2,
            b.y2,
            b.hx,
            b.hy,
            cut="right",
        )

        glyph = ufoLib2.objects.Glyph()
        draw_corner(
            glyph.getPen(),
            dc.stroke_x,
            dc.stroke_y,
            b.x2,
            ymid,
            b.xmid,
            y1,
            b.hx,
            b.hy,
            orientation="bottom-left",
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.x1 - 10,
            0,
            b.x2 + 10,
            b.y2 + 10,
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)

        # draw_rect(pen, b.xmid, y1, b.x2 - dc.stroke_x, y1 + dc.stroke_y)
