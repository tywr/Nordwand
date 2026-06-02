from glyphs import Glyph
from draw.rect import draw_rect


class EqualsSignGlyph(Glyph):
    name = "equals_sign"
    unicode = "0x3D"
    width_ratio = 1
    gap = 0.4
    stroke_ratio = 0.92

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="x_height",
            width=dc.width * self.width_ratio + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        s = dc.stroke_x * self.stroke_ratio
        g = self.gap * b.height
        draw_rect(
            pen,
            b.x1,
            dc.math + g / 2 - s / 2,
            b.x2,
            dc.math + g / 2 + s / 2,
        )
        draw_rect(
            pen,
            b.x1,
            dc.math - g / 2 - s / 2,
            b.x2,
            dc.math - g / 2 + s / 2,
        )
