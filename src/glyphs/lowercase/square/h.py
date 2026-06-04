from draw.arch import draw_arch
from draw.rect import draw_rect

from glyphs.lowercase.square import SquareLowercaseGlyph


class LowercaseHGlyph(SquareLowercaseGlyph):
    name = "lowercase_h"
    unicode = "0x68"
    sbr = 0.87

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width=self.width_ratio * dc.width + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            overshoot_top=True,
        )
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
