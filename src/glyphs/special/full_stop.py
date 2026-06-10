from glyphs import Glyph
from draw.rect import draw_rect


class FullStopGlyph(Glyph):
    name = "full_stop"
    unicode = "0x2E"
    width_ratio = 0.265
    bold_width_ratio = 0.354
    taper = 0.5
    stroke_ratio = 1.2
    stroke_ratio_bold = 1
    bold_sbl = 1.154
    bold_sbr = 1.154

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        bw = max(0, dc.weight - 400) / 300
        sr = (1 - bw) * self.stroke_ratio + bw * self.stroke_ratio_bold
        s = sr * dc.stroke_x
        draw_rect(pen, b.xmid - s / 2, 0, b.xmid + s / 2, s)
