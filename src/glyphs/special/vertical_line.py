from glyphs import Glyph
from draw.rect import draw_rect


class VerticalLineGlyph(Glyph):
    name = "vertical_line"
    unicode = "0x7C"
    width_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="ascent",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        ymid = dc.parenthesis
        y1, y2 = ymid - dc.parenthesis_length / 2, ymid + dc.parenthesis_length / 2
        draw_rect(pen, b.xmid - dc.stroke_x/2, y1, b.xmid + dc.stroke_x / 2, y2)
