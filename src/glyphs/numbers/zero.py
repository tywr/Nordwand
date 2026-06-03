from glyphs.numbers import NumberGlyph
from draw.loop import draw_loop


class ZeroGlyph(NumberGlyph):
    name = "zero"
    unicode = "0x30"
    slash = 0.2
    width_ratio = 1.1
    hx_ratio = 1.2
    hy_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            overshoot_bottom=True,
            overshoot_top=True,
            number=True,
        )
        hx = self.hx_ratio * b.hx
        hy = self.hy_ratio * b.hy

        draw_loop(
            pen,
            dc.stroke_x * self.stroke_x_ratio,
            dc.stroke_y * self.stroke_y_ratio,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            hx,
            hy,
        )
