from glyphs import Glyph
from draw.rect import draw_rect


class LowLineGlyph(Glyph):
    name = "low_line"
    unicode = "0x5F"
    stroke_ratio = 0.8
    width_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="x_height",
            width=dc.width * self.width_ratio + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        s = self.stroke_ratio * dc.stroke_x
        draw_rect(pen, b.x1, -s, b.x2, 0)
