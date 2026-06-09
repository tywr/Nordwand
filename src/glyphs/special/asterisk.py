from glyphs import Glyph
from draw.rect import draw_rect


class AsteriskGlyph(Glyph):
    name = "asterisk"
    unicode = "0x2A"
    width_ratio = 0.7
    bold_width_ratio = 0.74
    stroke_ratio = 1
    vert_offset = 0.5
    sbl = 0.8
    sbr = 0.8

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        s = dc.stroke_alt * self.stroke_ratio
        ov = self.vert_offset * b.height
        ymid = b.ymid + ov
        draw_rect(
            pen,
            b.x1,
            ymid - s / 2,
            b.x2,
            ymid + s / 2,
            rotate=30,
        )
        draw_rect(
            pen,
            b.x1,
            ymid - s / 2,
            b.x2,
            ymid + s / 2,
            rotate=-30,
        )
        draw_rect(
            pen,
            b.xmid - s / 2,
            ymid - b.width / 2,
            b.xmid + s / 2,
            ymid + b.width / 2,
        )
