from draw.arch import draw_arch
from draw.rect import draw_rect
from glyphs.lowercase.single_story import SingleStoryLowercaseGlyph


class LowercaseBGlyph(SingleStoryLowercaseGlyph):
    name = "lowercase_b"
    unicode = "0x62"
    sbr = 0.628
    sbl = 1
    bold_width_ratio = 1.094
    bold_sbl = 1.000
    bold_sbr = 0.583

    def draw(
        self,
        pen,
        dc,
    ):
        b = self.body_bounds(dc)
        bsx, bsy = (
            self.bowl_stroke_x_ratio * dc.stroke_x,
            self.bowl_stroke_y_ratio * dc.stroke_y,
        )
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        dx = bsx - dc.stroke_x
        draw_arch(
            pen,
            bsx,
            bsy,
            b.x1 - dx,
            b.y1,
            b.x2,
            b.y2,
            hx,
            hy,
            taper=dc.taper * self.taper,
            side="left",
        )

        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, dc.ascent)
