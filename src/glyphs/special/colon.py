from glyphs import Glyph
from draw.rect import draw_rect


class ColonGlyph(Glyph):
    name = "colon"
    unicode = "0x3A"
    width_ratio = 1
    stroke_ratio = 1.5
    gap = 1

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        s = self.stroke_ratio * dc.stroke_x
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
