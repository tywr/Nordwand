import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.arch import draw_arch
from draw.rect import draw_rect


class LowercaseRGlyph(Glyph):
    name = "lowercase_r"
    unicode = "0x72"
    loop_ratio = 0.85
    hx_ratio = 1.00
    hy_ratio = 0.85
    taper = 0.5
    width_ratio = 0.5
    stroke_ratio = 0.85
    arch_length = 0.92
    hx_ratio = 1
    sbl = 1
    sbr = 0.5

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width=self.width_ratio * dc.width + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            overshoot_top=True,
        )
        hx, hy = dc.hx * self.hx_ratio, dc.hy * self.hy_ratio
        ys = b.y2 - self.loop_ratio * b.height

        glyph = ufoLib2.objects.Glyph()
        draw_arch(
            glyph.getPen(),
            dc.stroke_x,
            dc.stroke_x * self.stroke_ratio,
            b.x1,
            ys,
            b.x1 + dc.width * self.arch_length + dc.stroke_x,
            b.y2,
            hx * self.hx_ratio,
            hy,
            taper=self.taper * dc.taper,
            side="left",
            cut="bottom",
        )

        # Left stem
        draw_rect(glyph.getPen(), b.x1, 0, b.x1 + dc.stroke_x, dc.x_height)

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(cut_glyph.getPen(), b.x2, b.y1, b.x2 + b.width, b.y2)

        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
