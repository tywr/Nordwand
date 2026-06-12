from glyphs import Glyph
from draw.rect import draw_rect


class NumberSignGlyph(Glyph):
    name = "number_sign"
    unicode = "0x23"
    width_ratio = 1.32
    gap = 0.42
    bar_height_ratio = 1
    height = "cap"
    width_ratio = 1.238
    sbl = 0.174
    sbr = 0.169
    bold_width_ratio = 1.313
    bold_sbl = 0.231
    bold_sbr = 0.224

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        g = self.gap * b.width
        h = dc.ascent
        ymid = dc.ascent / 2
        sx, sy = dc.stroke_x / 2, dc.stroke_y / 2
        xm1, xm2 = b.xmid - g / 2, b.xmid + g / 2
        ym1, ym2 = ymid - g / 2, ymid + g / 2
        y1, y2 = ymid - h / 2, ymid + h / 2

        draw_rect(pen, xm1 - sx, y1, xm1 + sx, y2)
        draw_rect(pen, xm2 - sx, y1, xm2 + sx, y2)
        draw_rect(pen, b.x1, ym1 - sy, b.x2, ym1 + sy)
        draw_rect(pen, b.x1, ym2 - sy, b.x2, ym2 + sy)
