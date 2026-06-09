from glyphs.accents import Accent
from draw.parallelogramm import draw_parallelogramm


class Circumflex(Accent):
    name = "circumflex"
    unicode = "0x5E"
    height_ratio = 0.35
    width_ratio = 0.75
    bold_width_ratio = 0.77
    stroke_ratio = 1
    sbl = 0.81
    sbr = 0.81

    def draw_at(self, pen, dc, x, y):
        b = self.body_bounds(dc)
        h = self.height_ratio * dc.x_height
        w = b.width
        x1, x2, xmid = x - w / 2, x + w / 2, x
        y1, y2 = y - h / 2, y + h / 2
        d = self.stroke_ratio * dc.stroke_x
        ov = 0.5 * d

        draw_parallelogramm(
            pen,
            dc.stroke_alt,
            dc.stroke_alt,
            x1,
            y1,
            xmid + ov,
            y2,
            delta=d,
        )
        draw_parallelogramm(
            pen,
            dc.stroke_alt,
            dc.stroke_alt,
            x2,
            y1,
            xmid - ov,
            y2,
            direction="top-left",
            delta=d,
        )
