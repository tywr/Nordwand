from glyphs import Glyph
from draw.rect import draw_rect


class EmDashGlyph(Glyph):
    name = "em_dash"
    unicode = "0x2014"
    stroke_ratio = 0.85
    width_ratio = 1

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        s = dc.stroke_x * self.stroke_ratio
        w = dc.window_width
        x1, x2 = b.xmid - w / 2, b.xmid + w / 2
        draw_rect(pen, x1, dc.x_height / 2 + s / 2, x2, dc.x_height / 2 - s / 2)
