from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect


class UppercaseFGlyph(UppercaseGlyph):
    name = "uppercase_f"
    unicode = "0x46"
    mid_bar_ratio = 0.9
    mid_ratio = 0.48
    width_ratio = 0.88
    sbr = 0.65
    sbl = 1.09

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        ymid = self.mid_ratio * b.height

        # Vertical stem
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        # Top bar
        draw_rect(pen, b.x1, b.y2 - sy, b.x2, b.y2)
        # Middle bar
        draw_rect(
            pen,
            b.x1,
            ymid - sy / 2,
            b.x1 + self.mid_bar_ratio * b.width,
            ymid + sy / 2,
        )
