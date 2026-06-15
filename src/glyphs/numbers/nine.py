from math import sin, cos
from glyphs.numbers import NumberGlyph
from draw.loop import draw_loop
from draw.arch import draw_arch
from draw.polygon import draw_polygon
from draw.parallelogramm import draw_parallelogramm
from utils.pens import NullPen


class NineGlyph(NumberGlyph):
    name = "nine"
    unicode = "0x39"
    width_ratio = 1.018
    vertical_ratio = 0.66
    bottom_cut = 0.2
    taper = 0.8
    foot_x = 0.02
    joint_x = 1.4
    hx_ratio = 0.95
    hy_ratio = 0.95
    sbl = 0.450
    sbr = 0.450
    overshoot_top = True
    bold_width_ratio = 1.157
    bold_sbl = 0.470
    bold_sbr = 0.470

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        ymid = b.y2 - self.vertical_ratio * b.height
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy

        xf = b.x1 + self.foot_x * b.width
        xj = b.x2 - self.joint_x * sx

        # Upper loop
        params = draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            ymid,
            b.x2,
            b.y2,
            hx,
            hy * self.vertical_ratio,
            taper=self.taper * dc.taper,
            side="right",
            cut="top",
        )

        # Compute the intersection
        (_, y1), (_, y2) = params["outer"].intersection_x(x=xj)
        yj = min(y1, y2)

        # Draw dummy parallelogramm to get the angle
        theta, delta = draw_parallelogramm(
            NullPen(), sx, sy, xj, yj, xf, b.y1, direction="bottom-left"
        )

        draw_polygon(
            pen,
            points=[
                (xj, yj),
                (xj, yj),
                (b.x2, (b.y2 + ymid) / 2),
                (b.x2 - sx, (b.y2 + ymid) / 2),
                (b.x2 - sx, (b.y2 + ymid) / 2 - sy / 2),
            ],
        )

        lp = ((b.y1 - yj) ** 2 + (xj - xf) ** 2) ** 0.5
        dx = lp * cos(theta)
        dy = lp * sin(theta)
        xcm, ycm = xj + delta - 0.66 * dx, yj - 0.66 * dy
        xcp, ycp = xj + delta - 0.33 * dx, yj - 0.33 * dy

        pen.moveTo((xj, yj))
        pen.lineTo((xf + delta, b.y1))
        pen.lineTo((xf + 2 * delta, b.y1))
        pen.lineTo((xcm, ycm))
        pen.curveTo(
            (xcp, ycp),
            (b.x2, (b.y2 + ymid) / 2 - b.hx),
            (b.x2, (b.y2 + ymid) / 2),
        )

        draw_loop(
            pen,
            sx,
            sy,
            b.x1,
            ymid,
            b.x2,
            b.y2,
            hx,
            hy * self.vertical_ratio,
            cut="bottom",
        )
