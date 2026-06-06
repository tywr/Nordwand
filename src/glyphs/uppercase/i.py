from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect


class UppercaseIGlyph(UppercaseGlyph):
    name = "uppercase_i"
    unicode = "0x49"
    width_ratio = 0
    sbl = 1.09
    sbr = 1.09

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            uppercase=True,
        )
        sx = dc.stroke_x * self.stroke_x_ratio

        # Vertical stem (centered)
        draw_rect(pen, b.xmid - sx / 2, b.y1, b.xmid + sx / 2, b.y2)
