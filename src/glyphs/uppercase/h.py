from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect


class UppercaseHGlyph(UppercaseGlyph):
    name = "uppercase_h"
    unicode = "0x48"
    bar_height = 0.52
    width_ratio = 1.18

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            uppercase=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        yb = self.bar_height * b.height

        # Left stem
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        # Right stem
        draw_rect(pen, b.x2 - sx, b.y1, b.x2, b.y2)
        # Middle bar
        draw_rect(pen, b.x1, yb - sy / 2, b.x2, yb + sy / 2)
