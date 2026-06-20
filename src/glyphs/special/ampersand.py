from math import tan
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from glyphs import Glyph
from draw.loop import draw_loop
from draw.arch import draw_arch
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm
from utils.pens import NullPen


class AmpersandGlyph(Glyph):
    name = "ampersand"
    unicode = "0x26"
    upper_width = 0.8
    upper_height = 0.4

    height = "cap"
    overshoot_top = True
    overshoot_bottom = True
    stroke_x_ratio = 1.01
    stroke_y_ratio = 1.04

    mid_ratio = 0.52
    loop_ratio = 0.4
    loop_up_offset = 0.05
    hx_ratio = 0.8
    hy_ratio = 1
    hx_ratio_up = 0.75
    hy_ratio_up = 1
    right_stroke_x = 0.63
    right_stroke_y = 0.79

    width_ratio = 1.336
    sbl = 0.598
    sbr = 0.183
    bold_width_ratio = 1.463
    bold_sbl = 0.775
    bold_sbr = 0.394

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        ymid = b.y1 + self.mid_ratio * b.height
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y
        hx, hy = self.hx_ratio * b.hx, self.hy_ratio * b.hy
        hux, huy = self.hx_ratio_up * b.hx, self.hy_ratio_up * b.hy
        xl = b.x1 + 2 * b.width * self.loop_ratio
        xr, yr = (
            b.x1 + self.right_stroke_x * b.width,
            b.y1 + self.right_stroke_y * b.height,
        )
        ot = self.loop_up_offset * b.width
        draw_arch(
            pen,
            sx,
            sy,
            b.x1 + ot,
            ymid - sy / 2,
            xl - ot,
            b.y2,
            hux,
            huy * (1 - self.mid_ratio),
            taper=0.6,
            side="bottom",
            cut="right",
        )
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            xl,
            ymid + sy / 2,
            hx,
            hy * self.mid_ratio,
            taper=0.6,
            side="top",
            cut="right",
        )
        draw_rect(pen, (b.x1 + xl) / 2, ymid - sy / 2, b.x2, ymid + sy / 2)
        draw_rect(
            pen,
            (b.x1 + xl) / 2,
            b.y1,
            xr,
            b.y1 + sy,
        )
        draw_rect(
            pen,
            (b.x1 + xl) / 2,
            b.y2 - sy,
            xr,
            b.y2,
        )
        draw_rect(
            pen,
            xr,
            b.y1,
            xr + sx,
            yr,
        )
