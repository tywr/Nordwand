from glyphs import Glyph
from draw.circle import draw_circle


class DegreeSignGlyph(Glyph):
    name = "degree_sign"
    unicode = "0xB0"
    h_offset = 0.2
    width = 0.4
    stroke_ratio = 0.65
    width_ratio = 1
    height = "cap"
    bold_width_ratio = 0.773
    bold_sbl = 0.718
    bold_sbr = 0.718

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        s = self.stroke_ratio * dc.stroke_x
        w = self.width * b.width
        o = self.h_offset * b.height

        draw_circle(pen, b.xmid, b.y2 - o, w / 2 + s, clockwise=False)
        draw_circle(pen, b.xmid, b.y2 - o, w / 2, clockwise=True)
