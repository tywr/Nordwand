from glyphs import Glyph
from draw.rect import draw_rect


class LowLineGlyph(Glyph):
    name = "low_line"
    unicode = "0x5F"
    stroke_ratio = 0.8
    width_ratio = 1.010
    sbl = -0.012
    sbr = -0.012
    bold_width_ratio = 0.914
    bold_sbl = 0.028
    bold_sbr = 0.028


    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        s = self.stroke_ratio * dc.stroke_x
        draw_rect(pen, b.x1, -s, b.x2, 0)
