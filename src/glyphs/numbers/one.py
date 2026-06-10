from glyphs.numbers import NumberGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm_vertical


class OneGlyph(NumberGlyph):
    name = "one"
    unicode = "0x31"
    branch_height = 0.34
    width_ratio = 0.566
    sbl = 0.762
    sbr = 1.488
    bold_width_ratio = 0.679
    bold_sbl = 0.814
    bold_sbr = 1.583

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        # Vertical stem (centered)
        draw_rect(pen, b.x2 - sx, b.y1, b.x2, b.y2)

        theta, delta = draw_parallelogramm_vertical(
            pen,
            sx,
            sy,
            b.x1,
            b.y1 + b.height * (1 - self.branch_height),
            b.x2 - sx,
            b.y2,
        )
