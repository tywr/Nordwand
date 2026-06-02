from glyphs import Glyph
from draw.rect import draw_rect


class EnDashGlyph(Glyph):
    name = "en_dash"
    unicode = "0x2013"
    width = 440
    stroke_ratio = 0.85
    width_ratio = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width=dc.width * self.width_ratio + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        w = self.width
        s = dc.stroke_x * self.stroke_ratio
        draw_rect(
            pen,
            b.xmid - w / 2,
            dc.x_height / 2 + s / 2,
            b.xmid + w / 2,
            dc.x_height / 2 - s / 2,
        )
