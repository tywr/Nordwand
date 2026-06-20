from glyphs.numbers import NumberGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class SevenGlyph(NumberGlyph):
    name = "seven"
    unicode = "0x37"
    offset_foot = 0.3
    width_ratio = 0.936
    sbl = 0.610
    sbr = 0.793
    bold_width_ratio = 1.032
    bold_sbl = 0.676
    bold_sbr = 0.944

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        ox = self.offset_foot * b.width

        # Top bar
        draw_rect(pen, b.x1, b.y2 - sy, b.x2, b.y2)

        # Diagonal stroke
        theta, delta = draw_parallelogramm(
            pen,
            sx,
            sy,
            b.x1 + ox,
            b.y1,
            b.x2,
            b.y2 - sy,
        )
