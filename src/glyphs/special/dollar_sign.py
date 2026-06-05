from glyphs import Glyph
from draw.rect import draw_rect


class DollarSignGlyph(Glyph):
    name = "dollar_sign"
    unicode = "0x24"
    width_ratio = 1
    overflow_ratio = 0.2

    def draw(self, pen, dc):
        from glyphs.uppercase.s import UppercaseSGlyph

        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        sg = UppercaseSGlyph()
        sg.draw(pen, dc)

        dh = self.overflow_ratio * b.height
        draw_rect(
            pen,
            b.xmid - dc.stroke_x / 2,
            b.y2 - dc.stroke_y / 2,
            b.xmid + dc.stroke_x / 2,
            b.y2 + dh,
        )
        draw_rect(
            pen,
            b.xmid - dc.stroke_x / 2,
            b.y1 - dh,
            b.xmid + dc.stroke_x / 2,
            b.y1 + dc.stroke_y / 2,
        )
