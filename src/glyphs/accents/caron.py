from glyphs.accents import Accent
from draw.parallelogramm import draw_parallelogramm


class Caron(Accent):
    name = "caron"
    unicode = "0x2C7"
    height_ratio = 0.35
    width_ratio = 0.75
    stroke_ratio = 1
    sbl = 0.81
    sbr = 0.81
    bold_width_ratio = 0.78
    bold_sbl = 0.81
    bold_sbr = 0.81

    def draw_at(self, pen, dc, x, y):
        b = self.body_bounds(dc)
        h = self.height_ratio * dc.x_height
        w = b.width
        x1, x2, xmid = x - w / 2, x + w / 2, x
        y1, y2 = y - h / 2, y + h / 2
        sx = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.25)
        ov = 0.5 * sx

        draw_parallelogramm(
            pen,
            dc.stroke_alt,
            dc.stroke_alt,
            xmid + ov,
            y1,
            x1,
            y2,
            direction="top-left",
            delta=sx,
        )
        draw_parallelogramm(
            pen,
            dc.stroke_alt,
            dc.stroke_alt,
            xmid - ov,
            y1,
            x2,
            y2,
            direction="top-right",
            delta=sx,
        )
