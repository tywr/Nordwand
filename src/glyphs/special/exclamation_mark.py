from glyphs import Glyph
from draw.polygon import draw_polygon
from draw.rect import draw_rect


class ExclamationMarkGlyph(Glyph):
    name = "exclamation_mark"
    unicode = "0x21"
    width_ratio = 0.217
    gap = 0.3
    height_overflow = 0.05
    stroke_ratio = 1
    dot_stroke_ratio = 1.1
    taper_length = 0.2
    taper = 0.85
    sbl = 1.159
    sbr = 1.159
    height = "cap"
    bold_width_ratio = 0.308
    bold_sbl = 1.197
    bold_sbr = 1.197

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx = dc.stroke_x * self.stroke_ratio
        sd = dc.stroke_x * self.dot_stroke_ratio
        g = self.gap * b.height
        dh = self.height_overflow * b.height
        h = b.y2 + dh - b.y1 - g

        draw_rect(
            pen,
            b.xmid - dc.stroke_x / 2,
            b.y1 + g + h * self.taper_length,
            b.xmid + dc.stroke_x / 2,
            b.y2 + dh,
        )
        draw_polygon(
            pen,
            points=[
                (b.xmid + sx / 2, b.y1 + g + h * self.taper_length),
                (b.xmid - sx / 2, b.y1 + g + h * self.taper_length),
                (b.xmid - self.taper * sx / 2, b.y1 + g),
                (b.xmid + self.taper * sx / 2, b.y1 + g),
            ],
        )

        draw_rect(pen, b.xmid - sd / 2, 0, b.xmid + sd / 2, sd)
