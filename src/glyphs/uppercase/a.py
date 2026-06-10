from math import cos
from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect


class UppercaseAGlyph(UppercaseGlyph):
    name = "uppercase_a"
    unicode = "0x41"
    bar_height = 0.39
    overlap = 0.5
    stroke_x_ratio = 1.01
    width_ratio = 1.25
    bold_width_ratio = 1.367
    sbl = 0.4
    sbr = 0.4
    bold_sbl = 0.462
    bold_sbr = 0.449

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        half_width = b.width / 2 - sx / 2
        ov = 0.5 * dc.stroke_x
        hb = self.bar_height * b.height

        # Left branch
        draw_parallelogramm(
            pen,
            sx,
            sy,
            b.x2,
            b.y1,
            b.xmid - ov,
            b.y2,
            direction="top-left",
        )
        # Right branch
        theta, delta = draw_parallelogramm(pen, sx, sy, b.x1, b.y1, b.xmid + ov, b.y2)

        # Crossbar
        draw_rect(
            pen,
            b.xmid - half_width + (hb - sy) * cos(theta),
            hb - sy,
            b.xmid + half_width - (hb - sy) * cos(theta),
            hb,
        )
