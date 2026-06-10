from glyphs.uppercase import UppercaseGlyph
from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect


class UppercaseYGlyph(UppercaseGlyph):
    name = "uppercase_y"
    unicode = "0x59"
    width_ratio = 1.211
    bold_width_ratio = 1.31
    junction_ratio = 0.39
    stroke_x_ratio = 1.15
    sbr = 0.401
    sbl = 0.401

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx = dc.stroke_x * self.stroke_x_ratio

        yj = b.x1 + self.junction_ratio * b.height

        draw_rect(pen, b.xmid - sx / 2, b.y1, b.xmid + sx / 2, yj)

        draw_parallelogramm(pen, sx, sx, b.xmid - sx / 2, yj, b.x2, b.y2, delta=sx)
        draw_parallelogramm(
            pen,
            sx,
            sx,
            b.xmid + sx / 2,
            yj,
            b.x1,
            b.y2,
            direction="top-left",
            delta=sx,
        )
