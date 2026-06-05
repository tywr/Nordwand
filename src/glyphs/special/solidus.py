from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class SolidusGlyph(Glyph):
    name = "solidus"
    unicode = "0x2F"
    width_ratio = 1
    height_ratio = 0.8

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="ascent",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        ymid = dc.parenthesis
        h = self.height_ratio * dc.parenthesis_length
        draw_parallelogramm(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            ymid - h / 2,
            b.x2,
            ymid + h / 2,
        )
