from draw.arch import draw_arch
from draw.rect import draw_rect

from glyphs.lowercase.square import SquareLowercaseGlyph


class LowercaseHGlyph(SquareLowercaseGlyph):
    name = "lowercase_h"
    unicode = "0x68"
    sbr = 0.884
    overshoot_top = True

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        yl = b.y2 - self.loop_ratio * b.height

        # Top arch, cut at the bottom (only upper half drawn)
        draw_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            yl,
            b.x2,
            b.y2,
            self.hx_ratio * b.hx,
            b.hy,
            taper=self.taper * dc.taper,
            side="left",
            cut="bottom",
        )
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, dc.ascent)

        # Right stem — reaches up to the arch midpoint
        draw_rect(pen, b.x2 - dc.stroke_x, 0, b.x2, (b.y2 + yl) / 2)
