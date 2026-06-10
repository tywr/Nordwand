from glyphs.numbers import NumberGlyph
from draw.arch import draw_arch
from draw.rect import draw_rect


class EightGlyph(NumberGlyph):
    name = "eight"
    unicode = "0x38"
    height_ratio = 0.52
    loop_width_ratio = 0.92
    taper_top = 0.9
    taper_bot = 1.2
    hx_ratio = 0.9
    hy_ratio = 1
    extra_overshoot = 0.000
    width_ratio = 1.054
    sbl = 0.756
    sbr = 0.756
    overshoot_top = True
    overshoot_bottom = True
    bold_width_ratio = 1.180
    bold_sbl = 0.801
    bold_sbr = 0.795

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = b.hx * self.hx_ratio, b.hy * self.hy_ratio
        ymid = b.y1 + b.height * self.height_ratio
        wtop = self.loop_width_ratio * b.width
        dtop = (b.width - wtop) / 2
        ov = self.extra_overshoot * b.height

        # Top loop
        draw_arch(
            pen,
            sx,
            sy,
            b.x1 + dtop,
            ymid - sy / 2,
            b.x2 - dtop,
            b.y2 + ov,
            hx,
            hy * (1 - self.height_ratio),
            taper=self.taper_top * dc.taper,
            side="bottom",
        )

        # Bottom loop
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1 - ov,
            b.x2,
            ymid + sy / 2,
            hx,
            hy * self.height_ratio,
            taper=self.taper_bot * dc.taper,
            side="top",
        )
