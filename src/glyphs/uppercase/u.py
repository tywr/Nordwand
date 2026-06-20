from glyphs.uppercase import UppercaseGlyph
from draw.loop import draw_loop
from draw.rect import draw_rect


class UppercaseUGlyph(UppercaseGlyph):
    name = "uppercase_u"
    unicode = "0x55"
    hx_ratio = 1.0
    hy_ratio = 1.0
    width_ratio = 1.167
    bold_width_ratio = 1.278
    loop_ratio = 0.66
    sbl = 1.085
    sbr = 1.085
    overshoot_bottom = True
    bold_sbl = 1.127
    bold_sbr = 1.127

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        y2 = self.loop_ratio * b.height
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy * self.loop_ratio

        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, y2, hx, hy, cut="top")

        draw_rect(pen, b.x1, (b.y1 + y2) / 2, b.x1 + sx, b.y2)
        draw_rect(pen, b.x2 - sx, (b.y1 + y2) / 2, b.x2, b.y2)
