from glyphs import Glyph
from draw.rect import draw_rect


class ApostropheMarkGlyph(Glyph):
    name = "apostrophe"
    unicode = "0x27"
    width_ratio = 0
    height_ratio = 0.7

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="x_height",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        h = self.height_ratio * b.height
        s = dc.stroke_x
        draw_rect(pen, b.xmid - s / 2, dc.ascent - h, b.xmid + s / 2, dc.ascent)
