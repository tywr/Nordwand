from draw.loop import draw_loop
from glyphs.lowercase.round import RoundLowercaseGlyph


class LowercaseOGlyph(RoundLowercaseGlyph):
    name = "lowercase_o"
    unicode = "0x6F"
    width_ratio = 1.0

    def draw(
        self,
        pen,
        dc,
    ):
        b = dc.body_bounds(
            width=self.width_ratio * dc.width + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            overshoot_bottom=True,
            overshoot_top=True,
        )
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        draw_loop(pen, sx, sy, b.x1, b.y1, b.x2, b.y2, b.hx, b.hy)
