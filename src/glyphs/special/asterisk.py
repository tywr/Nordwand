from glyphs import Glyph
from draw.rect import draw_rect


class AsteriskGlyph(Glyph):
    name = "asterisk"
    unicode = "0x2A"
    width_ratio = 1.31
    stroke_ratio = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="x_height",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        s = dc.stroke_alt * self.stroke_ratio
        ymid = dc.math
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
