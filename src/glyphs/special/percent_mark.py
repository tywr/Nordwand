from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm
from draw.loop import draw_loop


class PercentMarkGlyph(Glyph):
    name = "percent_mark"
    unicode = "0x25"
    offset_ratio_x = 0.14
    offset_ratio_y = 0.51
    zero_ratio = 0.5
    height = "cap"
    width_ratio = 1.722
    sbl = 0.378
    sbr = 0.378
    bold_width_ratio = 1.765
    bold_sbl = 0.324
    bold_sbr = 0.324

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        h = self.zero_ratio * b.height
        w = self.zero_ratio * b.width
        ox = self.offset_ratio_x * b.width
        oy = self.offset_ratio_y * b.height

        draw_parallelogramm(pen, dc.stroke_x, dc.stroke_y, b.x1, b.y1, b.x2, b.y2)
        draw_loop(
            pen,
            dc.stroke_alt,
            dc.stroke_alt,
            b.x1 + ox / 2 - w / 2,
            b.y2 - oy / 2 - h / 2,
            b.x1 + ox / 2 + w / 2,
            b.y2 - oy / 2 + h / 2,
            b.hx * self.zero_ratio,
            b.hy * self.zero_ratio,
        )
        draw_loop(
            pen,
            dc.stroke_alt,
            dc.stroke_alt,
            b.x2 - ox / 2 - w / 2,
            b.y1 + oy / 2 - h / 2,
            b.x2 - ox / 2 + w / 2,
            b.y1 + oy / 2 + h / 2,
            b.hx * self.zero_ratio,
            b.hy * self.zero_ratio,
        )
