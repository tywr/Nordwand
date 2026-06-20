from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class UppercaseZGlyph(UppercaseGlyph):
    name = "uppercase_z"
    unicode = "0x5A"
    right_offset = 0.01
    left_offset = 0.01
    width_ratio = 1.091
    bold_width_ratio = 1.187
    sbl = 0.256
    sbr = 0.256
    bold_sbl = 0.282
    bold_sbr = 0.282

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        xl = b.x1 + self.left_offset * b.width
        xr = b.x2 - self.right_offset * b.width

        # Top and bottom bars
        draw_rect(pen, xl, b.y2 - sy, xr, b.y2)
        draw_rect(pen, b.x1, 0, b.x2, sy)

        # Diagonal stroke
        theta, delta = draw_parallelogramm(
            pen,
            sx,
            sy,
            b.x1,
            b.y1 + sy,
            xr,
            b.y2 - sy,
        )
