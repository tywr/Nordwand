import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.corner import draw_corner
from glyphs.lowercase.single_story import SingleStoryLowercaseGlyph


class LowercaseGGlyph(SingleStoryLowercaseGlyph):
    name = "lowercase_g"
    unicode = "0x67"
    sbl = 0.63
    sbr = 0.94

    tail_offset = 0
    tail_stroke_x_ratio = 0.96
    tail_stroke_y_ratio = 1.01
    hx_ratio = 1.0
    hy_ratio = 0.92
    tail_hx_ratio = 1
    tail_hy_ratio = 0.6
    cut_ratio = 0.265
    tail_offset = 0.04
    y1_offset = 0.065

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            overshoot_bottom=True,
            overshoot_top=True,
        )
        hx, hy = (self.hx_ratio * b.hx, self.hy_ratio * b.hy)
        bsx, bsy = (
            self.bowl_stroke_x_ratio * dc.stroke_x,
            self.bowl_stroke_y_ratio * dc.stroke_y,
        )
        tsx, tsy = (
            self.tail_stroke_x_ratio * dc.stroke_x,
            self.tail_stroke_y_ratio * dc.stroke_y,
        )
        thx, thy = (
            self.tail_hx_ratio * dc.hx,
            self.tail_hy_ratio * dc.hy,
        )
        xt = b.x1 + self.tail_offset * b.width
        y1 = b.y1 + self.y1_offset * b.height

        # Bowl (open on the right, mirrored from b)
        draw_arch(
            pen,
            bsx,
            bsy,
            b.x1,
            y1,
            b.x2,
            b.y2,
            hx,
            hy,
            taper=dc.taper * self.taper,
            side="right",
        )

        # Right stem with gap at baseline and dent inset
        draw_rect(pen, b.x2 - dc.stroke_x, 0, b.x2, dc.x_height)

        # Corner curving down-left into the descender
        draw_corner(
            pen,
            dc.stroke_x,
            tsy,
            b.x2,
            0,
            b.xmid,
            dc.descent - dc.v_overshoot,
            thx,
            thy,
            orientation="bottom-left",
        )

        glyph = ufoLib2.objects.Glyph()
        draw_corner(
            glyph.getPen(),
            tsx,
            tsy,
            xt,
            0,
            b.xmid,
            dc.descent - dc.v_overshoot,
            thx,
            thy,
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.x1 - 10,
            dc.descent - dc.v_overshoot + b.height * self.cut_ratio,
            b.xmid,
            b.ymid,
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
