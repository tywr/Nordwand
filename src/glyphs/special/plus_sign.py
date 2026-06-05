from glyphs import Glyph
from draw.rect import draw_rect


class PlusSignGlyph(Glyph):
    name = "plus_sign"
    unicode = "0x2B"
    width_ratio = 1
    stroke_ratio = 0.88

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        s = dc.stroke_x * self.stroke_ratio

        draw_rect(pen, b.x1, dc.math - s / 2, b.x2, dc.math + s / 2)
        draw_rect(pen, b.xmid - s / 2, dc.math - b.width / 2, b.xmid + s / 2, dc.math + b.width / 2)
