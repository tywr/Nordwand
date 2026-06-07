from glyphs import Glyph
from draw.rect import draw_rect


class DollarSignGlyph(Glyph):
    name = "dollar_sign"
    unicode = "0x24"
    width_ratio = 1
    overflow_ratio = 0.2
    height = "cap"

    def draw(self, pen, dc):
        from glyphs.uppercase.s import UppercaseSGlyph

        b = self.body_bounds(dc)
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
