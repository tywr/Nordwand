from glyphs.numbers import NumberGlyph
from draw.loop import draw_loop


class ZeroGlyph(NumberGlyph):
    name = "zero"
    unicode = "0x30"
    slash = 0.2
    width_ratio = 0.982
    bold_width_ratio = 1.004
    hx_ratio = 1
    hy_ratio = 1
    overshoot_top = True
    overshoot_bottom = True
    sbl = 0.561
    sbr = 0.561
    bold_sbl = 0.549
    bold_sbr = 0.549

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        hx = self.hx_ratio * b.hx
        hy = self.hy_ratio * b.hy

        draw_loop(
            pen,
            dc.stroke_x * self.stroke_x_ratio,
            dc.stroke_y * self.stroke_y_ratio,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            hx,
            hy,
        )
