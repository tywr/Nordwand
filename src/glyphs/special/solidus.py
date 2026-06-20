from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class SolidusGlyph(Glyph):
    name = "solidus"
    unicode = "0x2F"
    height_ratio = 0.8
    height = "ascent"
    width_ratio = 0.624
    sbl = -0.122
    sbr = -0.122
    bold_width_ratio = 0.600
    bold_sbl = -0.324
    bold_sbr = -0.324

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            dc.descent,
            b.x2,
            dc.ascent,
        )
