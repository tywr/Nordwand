from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class ReverseSolidusGlyph(Glyph):
    name = "reverse_solidus"
    unicode = "0x5C"
    width_ratio = 1
    height_ratio = 0.8
    height = "ascent"
    bold_width_ratio = 0.690
    bold_sbl = 0.000
    bold_sbr = 0.000

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        ymid = dc.parenthesis
        h = self.height_ratio * dc.parenthesis_length
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2,
            ymid - h / 2,
            b.x1,
            ymid + h / 2,
            direction="top-left"
        )
