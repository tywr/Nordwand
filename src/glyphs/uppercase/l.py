from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect


class UppercaseLGlyph(UppercaseGlyph):
    name = "uppercase_l"
    unicode = "0x4C"
    width_ratio = 0.903
    bold_width_ratio = 0.903
    sbl = 1.195
    sbr = 0.256
    bold_sbl = 1.169
    bold_sbr = 0.225


    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        # Vertical stem
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        # Bottom bar
        draw_rect(pen, b.x1, b.y1, b.x2, b.y1 + sy)
