from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.loop import draw_loop


class UppercaseJGlyph(UppercaseGlyph):
    name = "uppercase_j"
    unicode = "0x4A"
    cap_ratio = 1
    hx_ratio = 1.1
    hy_ratio = 0.45
    loop_ratio = 0.5
    tail_len = 0.5
    width_ratio = 0.838
    sbl = 0.5
    sbr = 1.07
    overshoot_bottom = True

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        yl = b.y1 + self.loop_ratio * b.height

        # Vertical stem (centered)
        draw_rect(pen, b.x2 - sx, (b.y1 + yl) / 2, b.x2, b.y2)

        # Corner to bottom
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            yl,
            hx,
            hy,
            cut="top",
        )
