from glyphs import Glyph
from draw.rect import draw_rect
from draw.polygon import draw_polygon


class SemiColonGlyph(Glyph):
    name = "semi_colon"
    unicode = "0x3B"
    width_ratio = 1
    stroke_ratio = 1.5
    gap = 1

    def draw(self, pen, dc):
        from glyphs.special.comma import CommaGlyph

        b = dc.body_bounds(
            height="x_height",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        s = self.stroke_ratio * dc.stroke_x
        g = b.height * self.gap

        draw_rect(
            pen,
            b.xmid - s / 2,
            b.y1 + g - s,
            b.xmid + s / 2,
            b.y1 + g,
        )
        cg = CommaGlyph()
        cg.draw(pen, dc)
