from glyphs import Glyph
from draw.rect import draw_rect


class ColonGlyph(Glyph):
    name = "colon"
    unicode = "0x3A"
    width_ratio = 0.265
    bold_width_ratio = 0.354
    stroke_ratio = 1.2
    stroke_ratio_bold = 1
    gap = 0.935
    bold_sbl = 1.154
    bold_sbr = 1.154

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        bw = max(0, dc.weight - 400) / 300
        sr = (1 - bw) * self.stroke_ratio + bw * self.stroke_ratio_bold
        s = sr * dc.stroke_x
        g = b.height * self.gap

        draw_rect(
            pen,
            b.xmid - s / 2,
            b.y1,
            b.xmid + s / 2,
            b.y1 + s,
        )
        draw_rect(
            pen,
            b.xmid - s / 2,
            b.y1 + g - s,
            b.xmid + s / 2,
            b.y1 + g,
        )
