from glyphs import Glyph
from draw.rect import draw_rect


class ApostropheMarkGlyph(Glyph):
    name = "apostrophe"
    unicode = "0x27"
    sbl = 1.159
    sbr = 1.159
    bold_width_ratio = 0.228
    width_ratio = 0.175
    height_ratio = 0.6
    bold_sbl = 1.197
    bold_sbr = 1.197

    def draw(self, pen, dc):
        ec = self.extra_cut(dc)
        b = self.body_bounds(dc)
        h = self.height_ratio * b.height
        s = dc.stroke_x
        draw_rect(pen, b.xmid - s / 2, dc.ascent - h - ec, b.xmid + s / 2, dc.cap)
