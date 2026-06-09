from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class LowercaseXGlyph(Glyph):
    name = "lowercase_x"
    unicode = "0x78"
    width_ratio = 0.933
    bold_width_ratio = 1.045
    sbl = 0.43
    sbr = 0.43

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        draw_parallelogramm(pen, dc.stroke_x, dc.stroke_y, b.x1, b.y1, b.x2, b.y2)
        theta, delta = draw_parallelogramm(
            pen, dc.stroke_x, dc.stroke_y, b.x2, b.y1, b.x1, b.y2, direction="top-left"
        )
