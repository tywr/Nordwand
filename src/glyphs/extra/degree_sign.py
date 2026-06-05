from glyphs import Glyph
from draw.circle import draw_circle


class DegreeSignGlyph(Glyph):
    name = "degree_sign"
    unicode = "0xB0"
    h_offset = 0.2
    width = 0.4
    stroke_ratio = 0.65
    width_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        s = self.stroke_ratio * dc.stroke_x
        w = self.width * b.width
        o = self.h_offset * b.height

        draw_circle(pen, b.xmid, b.y2 - o, w / 2 + s, clockwise=False)
        draw_circle(pen, b.xmid, b.y2 - o, w / 2, clockwise=True)
