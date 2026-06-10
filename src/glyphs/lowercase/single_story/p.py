from draw.arch import draw_arch
from draw.rect import draw_rect
from glyphs.lowercase.single_story import SingleStoryLowercaseGlyph


class LowercasePGlyph(SingleStoryLowercaseGlyph):
    name = "lowercase_p"
    unicode = "0x70"
    sbl = 0.942
    sbr = 0.640
    bold_width_ratio = 1.094
    bold_sbl = 0.936
    bold_sbr = 0.590

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        bsx, bsy = (
            self.bowl_stroke_x_ratio * dc.stroke_x,
            self.bowl_stroke_y_ratio * dc.stroke_y,
        )
        dx = bsx - dc.stroke_x
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy

        # Bowl (open on the left, same as b)
        arch_params = draw_arch(
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

        draw_rect(pen, b.x1, dc.descent, b.x1 + dc.stroke_x, dc.x_height)
