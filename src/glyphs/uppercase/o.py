from glyphs.uppercase import UppercaseGlyph
from draw.loop import draw_loop


class UppercaseOGlyph(UppercaseGlyph):
    name = "uppercase_o"
    unicode = "0x4F"
    stroke_x_ratio = UppercaseGlyph.stroke_x_ratio * 1.04
    stroke_y_ratio = UppercaseGlyph.stroke_y_ratio * 1.09
    width_ratio = 1.314
    bold_width_ratio = 1.390
    sbl = 0.622
    sbr = 0.622
    overshoot_bottom = True
    overshoot_top = True
    bold_sbl = 0.620
    bold_sbr = 0.620

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
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
