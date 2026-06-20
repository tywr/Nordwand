from math import cos, sin
from glyphs.numbers import NumberGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm
from draw.loop import draw_loop
from utils.pens import NullPen


class TwoGlyph(NumberGlyph):
    name = "two"
    unicode = "0x32"
    width_ratio = 0.932
    loop_offset = 0.02
    hx_ratio = 1
    hy_ratio = 0.85
    xj_ratio = 0.68
    yj_ratio = 0.46
    internal_radius = 0.25
    sbl = 0.634
    sbr = 0.793
    overshoot_top = True
    bold_width_ratio = 0.953
    bold_sbl = 0.620
    bold_sbr = 0.873

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        xj = b.x1 + self.xj_ratio * b.width + sx / 2
        yj = b.y1 + self.yj_ratio * b.height
        yt = (b.ymid + b.y2) / 2
        ih = self.internal_radius * b.height
        x2 = b.x2 - self.loop_offset * b.width

        # Top arch
        params = draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.ymid,
            x2,
            b.y2,
            hx,
            hy / 2,
            cut="bottom",
        )
        ishy = params["inner"].hy
        oshy = params["outer"].hy

        theta, delta = draw_parallelogramm(
            NullPen(),
            sx,
            sy,
            b.x1,
            b.y1 + sy,
            xj,
            yj,
        )

        eps = theta
        px, py = delta * sin(eps) * cos(eps), delta * sin(eps) ** 2
        xl = xj - px
        yl = yj - py

        ihx, ihy = ih * cos(theta), ih * sin(theta)

        pen.moveTo((xl, yl))
        pen.curveTo((xl + ihx, yl + ihy), (x2, yt - oshy), (x2, yt))
        pen.lineTo((x2 - sx, yt))
        pen.curveTo(
            (x2 - sx, yt - ishy),
            (xj - delta + ihx, yj + ihy),
            (xj - delta, yj),
        )
        pen.lineTo((b.x1, b.y1 + sy))
        pen.lineTo((b.x1 + delta, b.y1 + sy))
        pen.closePath()

        # Bottom bar
        draw_rect(pen, b.x1, 0, b.x2, sy)
