from glyphs import Glyph
from draw.parallelogramm import draw_parallelogramm
from draw.loop import draw_loop


class PercentMarkGlyph(Glyph):
    name = "percent_mark"
    unicode = "0x25"
    width_ratio = 1.2
    offset_ratio_x = 0.45
    offset_ratio_y = 0.45
    zero_ratio = 0.4

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
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
