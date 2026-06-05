from glyphs.uppercase import UppercaseGlyph
from draw.corner import draw_corner
from draw.rect import draw_rect


class UppercaseDGlyph(UppercaseGlyph):
    name = "uppercase_d"
    unicode = "0x44"
    arch_start = 0.5
    hy_ratio = 1
    width_ratio = 1.26
    sbl = 1
    sbr = 0.75

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            uppercase=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        cut_x = b.x1 + self.arch_start * b.width
        hx, hy = b.hx, b.hy * self.hy_ratio

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.cap)

        # Connecting bars
        draw_rect(pen, b.x1, b.y2 - sy, cut_x, b.y2)
        draw_rect(pen, b.x1, 0, cut_x, sy)

        # Corner
        draw_corner(
            pen,
            sx,
            sy,
            b.x2,
            b.ymid,
            cut_x,
            b.y2,
            hx,
            hy,
            orientation="top-left",
        )
        draw_corner(
            pen,
            sx,
            sy,
            b.x2,
            b.ymid,
            cut_x,
            b.y1,
            hx,
            hy,
            orientation="bottom-left",
        )
