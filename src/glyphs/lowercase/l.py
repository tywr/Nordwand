from glyphs import Glyph
from draw.rect import draw_rect


class LowercaseLGlyph(Glyph):
    name = "lowercase_l"
    unicode = "0x6C"
    width_ratio = 0
    sbl = 1
    sbr = 1

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        # Stem
        draw_rect(pen, b.xmid - dc.stroke_x / 2, 0, b.xmid + dc.stroke_x / 2, dc.ascent)
