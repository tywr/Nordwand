from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm


class LowercaseXGlyph(Glyph):
    name = "lowercase_x"
    unicode = "0x78"
    width_ratio = 0.94
    sbl = 0.4
    sbr = 0.4

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width=dc.width * self.width_ratio + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        draw_parallelogramm(pen, dc.stroke_x, dc.stroke_y, b.x1, b.y1, b.x2, b.y2)
        theta, delta = draw_parallelogramm(
            pen, dc.stroke_x, dc.stroke_y, b.x2, b.y1, b.x1, b.y2, direction="top-left"
        )
