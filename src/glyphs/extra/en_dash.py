from glyphs import Glyph
from draw.rect import draw_rect


class EnDashGlyph(Glyph):
    name = "en_dash"
    unicode = "0x2013"
    stroke_ratio = 0.85
    width_ratio = 1.04
    bold_width_ratio = 1.12
    height_ratio = 0.54
    sbl = 0.47
    sbr = 0.47

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        s = dc.stroke_x * self.stroke_ratio
        h = b.y1 + self.height_ratio * b.height
        draw_rect(
            pen,
            b.xmid - b.width / 2,
            h + s / 2,
            b.xmid + b.width / 2,
            h - s / 2,
        )
