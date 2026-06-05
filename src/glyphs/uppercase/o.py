from glyphs.uppercase import UppercaseGlyph
from draw.loop import draw_loop


class UppercaseOGlyph(UppercaseGlyph):
    name = "uppercase_o"
    unicode = "0x4F"
    stroke_x_ratio = UppercaseGlyph.stroke_x_ratio * 1.00
    stroke_y_ratio = UppercaseGlyph.stroke_y_ratio * 1.00
    width_ratio = 1.4
    sbl = 0.75
    sbr = 0.75

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            overshoot_bottom=True,
            overshoot_top=True,
            uppercase=True,
        )
        draw_loop(
            pen,
            dc.stroke_x * self.stroke_x_ratio,
            dc.stroke_y * self.stroke_y_ratio,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            b.hx,
            b.hy,
        )
