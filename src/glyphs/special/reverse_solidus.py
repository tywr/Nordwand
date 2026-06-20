from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class ReverseSolidusGlyph(Glyph):
    name = "reverse_solidus"
    unicode = "0x5C"
    width_ratio = 0.624
    height_ratio = 0.8
    height = "ascent"
    width_ratio = 0.627
    sbl = -0.122
    sbr = -0.122
    bold_width_ratio = 0.662
    bold_sbl = -0.324
    bold_sbr = -0.324

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2,
            dc.descent,
            b.x1,
            dc.ascent,
            direction="top-left"
        )
