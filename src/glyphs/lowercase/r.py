import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.arch import draw_arch
from draw.rect import draw_rect


class LowercaseRGlyph(Glyph):
    name = "lowercase_r"
    unicode = "0x72"
    loop_ratio = 1
    hx_ratio = 1
    hy_ratio = 1
    taper = 0.3
    width_ratio = 0.568
    bold_width_ratio = 0.69
    stroke_ratio = 0.95
    arch_length = 0.65
    hx_ratio = 1.2
    sbl = 0.942
    sbr = 0.308
    overshoot_top = True

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        hx, hy = dc.hx * self.hx_ratio, dc.hy * self.hy_ratio
        ys = b.y2 - self.loop_ratio * b.height
        arch_length = dc.width * self.arch_length + 2 * dc.stroke_x

        glyph = ufoLib2.objects.Glyph()
        draw_arch(
            glyph.getPen(),
            dc.stroke_x,
            dc.stroke_x * self.stroke_ratio,
            b.x1,
            ys,
            b.x1 + arch_length,
            b.y2,
            hx,
            hy,
            taper=self.taper * dc.taper,
            side="left",
            cut="bottom",
        )

        # Left stem
        draw_rect(glyph.getPen(), b.x1, 0, b.x1 + dc.stroke_x, dc.x_height)

        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(cut_glyph.getPen(), b.x2, b.y1 - 10, b.x2 + arch_length + 100, b.y2 + 10)

        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
