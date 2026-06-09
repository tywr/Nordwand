from glyphs.uppercase import UppercaseGlyph
from draw.loop import draw_loop
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class UppercaseRGlyph(UppercaseGlyph):
    name = "uppercase_r"
    unicode = "0x52"
    loop_ratio = 0.605
    loop_width = 0.96
    branch_start = 0.63
    width_ratio = 1.06
    bold_width_ratio = 1.16
    offset_bold = 50
    sbl = 1.07
    sbr = 0.58

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = b.hx * self.loop_width, b.hy * self.loop_ratio
        ymid = b.y1 + (1 - self.loop_ratio) * b.height
        xb = (
            self.branch_start * b.width
            - self.offset_bold * max(dc.weight - 400, 0) / 300
        )
        w = self.loop_width * b.width

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.cap)

        # Upper loop (narrower, displaced left)
        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            ymid,
            b.x1 + w,
            b.y2,
            hx,
            hy,
            cut="left",
        )

        # Connecting bars
        draw_rect(pen, b.x1, b.y2 - sy, b.x2 - b.width / 2, b.y2)
        draw_rect(
            pen,
            b.x1,
            ymid,
            b.x2 - b.width / 2,
            ymid + sy,
        )

        # Right stem
        draw_parallelogramm(
            pen,
            sx,
            sy,
            b.x2,
            0,
            xb,
            ymid + sy / 2,
            direction="top-left",
        )
