from draw.arch import draw_arch
from draw.rect import draw_rect
from glyphs.lowercase.square import SquareLowercaseGlyph


class LowercaseUGlyph(SquareLowercaseGlyph):
    name = "lowercase_u"
    unicode = "0x75"
    sbl = 0.87
    sbr = 0.94

    def draw(self, pen, dc):
        b = dc.body_bounds(
            width=self.width_ratio * dc.width + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            overshoot_bottom=True,
        )
        yl = b.y1 + self.loop_ratio * b.height

        # Bottom arch, cut at top (only lower half drawn)
        draw_arch(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y1,
            b.x2,
            yl,
            self.hx_ratio * b.hx,
            b.hy,
            taper=self.taper * dc.taper,
            side="right",
            cut="top",
        )

        draw_rect(pen, b.x2 - dc.stroke_x, 0, b.x2, dc.x_height)

        # Left stem — starts from arch midpoint
        draw_rect(pen, b.x1, (yl + b.y1) / 2, b.x1 + dc.stroke_x, dc.x_height)
