from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect


class UppercaseLGlyph(UppercaseGlyph):
    name = "uppercase_l"
    unicode = "0x4C"
    width_ratio = 0.86
    stroke_x_ratio = 1.00
    sbl = 1.07
    sbr = 0.67


    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            uppercase=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        # Vertical stem
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        # Bottom bar
        draw_rect(pen, b.x1, b.y1, b.x2, b.y1 + sy)
