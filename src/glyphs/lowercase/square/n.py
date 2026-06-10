from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.polygon import draw_polygon
from glyphs.lowercase.square import SquareLowercaseGlyph


class LowercaseNGlyph(SquareLowercaseGlyph):
    name = "lowercase_n"
    unicode = "0x6E"
    sbr = 0.884
    sbl = 0.942
    overshoot_top = True
    bold_width_ratio = 1.010
    bold_sbl = 0.936
    bold_sbr = 0.872

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

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + dc.stroke_x, dc.x_height)

        # Right stem — reaches up to the arch midpoint
        draw_rect(pen, b.x2 - dc.stroke_x, 0, b.x2, (b.y2 + yl) / 2)
