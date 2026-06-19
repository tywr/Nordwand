from glyphs.numbers import NumberGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class FourGlyph(NumberGlyph):
    name = "four"
    unicode = "0x34"
    horizontal_ratio = 0.715
    vertical_ratio = 0.315
    mid_bar_ratio = 1
    overlap = 0.22
    stroke_ratio = 0.93
    width_ratio = 1.1
    sbl = 0.68
    sbr = 0.64
    bold_width_ratio = 1.191
    bold_sbl = 0.692
    bold_sbr = 0.744

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        ov = self.overlap * sx

        xmid = b.x1 + self.horizontal_ratio * b.width
        ymid = b.y1 + self.vertical_ratio * b.height
        ybar = b.y1 + self.mid_bar_ratio * b.height

        sd = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.15)
        draw_parallelogramm(pen, sd, sd, b.x1, ymid, xmid + ov, b.y2)

        # Horizontal line
        draw_rect(pen, b.x1, ymid - sy, b.x2, ymid)

        # Vertical line
        draw_rect(pen, xmid - sx / 2, b.y1, xmid + sx / 2, ybar)
