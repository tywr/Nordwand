from glyphs import Glyph
from draw.circle import draw_circle


class DegreeSignGlyph(Glyph):
    name = "degree_sign"
    unicode = "0xB0"
    h_offset = 0.27
    stroke_ratio = 0.85
    height = "cap"
    width_ratio = 0.620
    sbl = 0.476
    sbr = 0.476
    bold_width_ratio = 0.668
    bold_sbl = 0.521
    bold_sbr = 0.521

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        s = self.stroke_ratio * dc.stroke_x
        w = b.width
        o = self.h_offset * b.height

        draw_circle(pen, b.xmid, b.y2 - o, w / 2, clockwise=False)
        draw_circle(pen, b.xmid, b.y2 - o, w / 2 - s, clockwise=True)
