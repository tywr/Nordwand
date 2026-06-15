import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from glyphs.numbers import NumberGlyph
from draw.arch import draw_arch
from draw.rect import draw_rect


class ThreeGlyph(NumberGlyph):
    name = "three"
    unicode = "0x33"
    loop_width_ratio = 0.92
    mid_ratio = 0.515
    taper_high = 1.5
    taper_low = 1.5
    len_mid = 0.7
    hx_ratio = 0.9
    hy_ratio = 0.9
    width_ratio = 1.018
    sbl = 0.820
    sbr = 0.762
    overshoot_top = True
    overshoot_bottom = True
    bold_width_ratio = 1.132
    bold_sbl = 0.788
    bold_sbr = 0.788

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = b.hx * self.hx_ratio, b.hy * self.hy_ratio

        ymid = b.y1 + self.mid_ratio * b.height
        xl = b.x1 + (1 - self.loop_width_ratio) * b.width / 2
        xr = b.x2 - (1 - self.loop_width_ratio) * b.width / 2
        base_glyph = ufoLib2.objects.Glyph()
        ry = (b.y2 - b.ymid + sy / 2) / b.height

        # Top loop
        top_params = draw_arch(
            base_glyph.getPen(),
            sx,
            sy,
            xl,
            ymid - sy / 2,
            xr,
            b.y2,
            hx,
            hy * ry * 2 * (1 - self.mid_ratio),
            taper=self.taper_high * dc.taper,
            side="bottom",
        )

        # Bottom loop
        draw_arch(
            base_glyph.getPen(),
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            ymid + sy / 2,
            hx,
            hy * ry * 2 * self.mid_ratio,
            taper=self.taper_low * dc.taper,
            side="top",
        )

        # Remove the left-middle part
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.x1,
            ymid - b.height / 4,
            b.x1 + b.width / 2,
            ymid + b.height / 4,
        )

        result = BooleanGlyph(base_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        # Extension of the middle bar
        draw_rect(
            pen,
            b.x1 + (1 - self.len_mid) * b.width,
            ymid - sy / 2,
            b.xmid,
            ymid + sy / 2,
        )
