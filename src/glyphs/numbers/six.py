from math import cos, sin
from glyphs.numbers import NumberGlyph
from draw.loop import draw_loop
from draw.arch import draw_arch
from draw.polygon import draw_polygon
from draw.parallelogramm import draw_parallelogramm
from utils.pens import NullPen


class SixGlyph(NumberGlyph):
    name = "six"
    unicode = "0x36"
    width_ratio = 1.018
    loop_ratio = 0.66
    top_ratio = 0.4
    taper = 0.6
    cap_x = 0.98
    hx_ratio = 0.95
    hy_ratio = 0.95
    joint_x = 1.4
    sbl = 0.720
    sbr = 0.720
    overshoot_bottom = True
    bold_width_ratio = 1.157
    bold_sbl = 0.801
    bold_sbr = 0.808

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy


        ymid = b.y1 + self.loop_ratio * b.height
        xc = b.x1 + self.cap_x * b.width
        xj = b.x1 + self.joint_x * sx

        # Bottom loop
        params = draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            ymid,
            hx,
            hy * self.loop_ratio,
            taper=self.taper * dc.taper,
            side="left",
            cut="bottom",
        )

        # Compute the intersection
        (_, y1), (_, y2) = params["outer"].intersection_x(x=xj)
        yj = max(y1, y2)

        theta, delta = draw_parallelogramm(
            NullPen(),
            sx,
            sy,
            xj,
            yj,
            xc,
            b.y2,
        )

        draw_polygon(
            pen,
            points=[
                (xj, yj),
                (xj - delta / 2, yj),
                (b.x1, (b.y1 + ymid) / 2),
                (b.x1 + sx, (b.y1 + ymid) / 2),
                (b.x1 + sx, (b.y1 + ymid) / 2 + sy / 2),
            ],
        )

        lp = ((b.y2 - yj) ** 2 + (xj - xc) ** 2) ** 0.5
        dx = lp * cos(theta)
        dy = lp * sin(theta)
        xcm, ycm = xj - delta + 0.66 * dx, yj + 0.66 * dy
        xcp, ycp = xj - delta + 0.33 * dx, yj + 0.33 * dy

        pen.moveTo((xj, yj))
        pen.lineTo((xc - delta, b.y2))
        pen.lineTo((xc - 2 * delta, b.y2))
        pen.lineTo((xcm, ycm))
        pen.curveTo(
            (xcp, ycp),
            (b.x1, (b.y1 + ymid) / 2 + b.hx),
            (b.x1, (b.y1 + ymid) / 2),
        )
        pen.lineTo((b.x1 + sx / 2, (b.y1 + ymid) / 2))
        pen.closePath()

        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            ymid,
            hx,
            hy * self.loop_ratio,
            cut="top",
        )
