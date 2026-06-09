from glyphs.accents import Accent
from draw.rect import draw_rect


class Macron(Accent):
    name = "macron"
    unicode = "0xAF"
    width_ratio = 0.665
    bold_width_ratio = 0.7
    stroke_ratio = 1
    sbl = 1.05
    sbr = 1.05

    def draw_at(self, pen, dc, x, y):
        b = self.body_bounds(dc)
        w = b.width
        t = self.stroke_ratio * dc.stroke_alt
        draw_rect(pen, x - w / 2, y - t / 2, x + w / 2, y + t / 2)
