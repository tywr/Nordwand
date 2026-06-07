from glyphs import Glyph
from draw.rect import draw_rect


class FullStopGlyph(Glyph):
    name = "full_stop"
    unicode = "0x2E"
    width_ratio = 0
    taper = 0.5
    stroke_ratio = 1.1

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        s = self.stroke_ratio * dc.stroke_x
        draw_rect(pen, b.xmid - s / 2, 0, b.xmid + s / 2, s)
