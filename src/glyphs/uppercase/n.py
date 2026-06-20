from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm_vertical


class UppercaseNGlyph(UppercaseGlyph):
    name = "uppercase_n"
    unicode = "0x4E"
    middle_stroke_ratio = 0.9
    overlap = 0.3
    width_ratio = 1.147
    bold_width_ratio = 1.274
    sbl = 1.195
    sbr = 1.195
    bold_sbl = 1.169
    bold_sbr = 1.169

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        # Vertical stems
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        draw_rect(pen, b.x2 - sx, b.y1, b.x2, b.y2)

        # Diagonal
        theta, delta = draw_parallelogramm_vertical(
            pen,
            sx * self.middle_stroke_ratio,
            sy * self.middle_stroke_ratio,
            b.x2 - sx,
            b.y1,
            b.x1 + sx,
            b.y2,
            direction="top-left",
        )
