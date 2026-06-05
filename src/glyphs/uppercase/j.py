from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.loop import draw_loop


class UppercaseJGlyph(UppercaseGlyph):
    name = "uppercase_j"
    unicode = "0x4A"
    cap_ratio = 1
    hx_ratio = 1
    loop_ratio = 0.56
    tail_len = 0.5
    width_ratio = 0.8
    sbl = 0.5
    sbr = 1.07

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            uppercase=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        xc = self.cap_ratio * b.width
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
            b.hx,
            self.loop_ratio * b.hy,
            cut="top",
        )
