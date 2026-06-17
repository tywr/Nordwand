import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph

from glyphs.numbers import NumberGlyph
from draw.arch import draw_arch
from draw.corner import draw_corner
from draw.parallelogramm import draw_parallelogramm
from draw.rect import draw_rect
from utils.pens import NullPen


class FiveGlyph(NumberGlyph):
    name = "five"
    unicode = "0x35"
    stroke_ratio = 0.88
    loop_ratio = 0.66
    junction_ratio = 0.43
    cap_offset = 0.08
    tilt = 0.23
    taper = 0.6
    ending_offset = 0.03
    thinning = 0.9
    overshoot_bottom = True
    width_ratio = 1.03
    sbl = 0.680
    sbr = 0.735
    bold_width_ratio = 1.18
    bold_sbl = 0.5
    bold_sbr = 0.7

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        sd = self.diag_stroke_dampening(self.stroke_ratio, dc.stroke_x, coef=0.15)
        yj = b.y1 + b.height * self.junction_ratio
        ew = 0.3 * max(dc.stroke_x - 90, 0)
        oj = self.tilt * b.width + ew
        xc = b.x2 - self.cap_offset * b.width
        xe = b.x1 + self.ending_offset * b.width + ew

        base_glyph = ufoLib2.objects.Glyph()

        # Bottom loop
        # params = draw_loop(
        #     base_glyph.getPen(),
        #     sx,
        #     sy,
        #     b.x1,
        #     b.y1,
        #     b.x2,
        #     b.y1 + b.height * self.loop_ratio,
        #     b.hx,
        #     b.hy * self.loop_ratio,
        #     cut="top",
        # )
        draw_corner(
            pen,
            sx,
            sy,
            b.x2,
            (b.y1 + b.height * self.loop_ratio) / 2,
            b.xmid,
            b.y1,
            b.hx,
            b.hy * self.loop_ratio,
            orientation="bottom-left",
        )
        draw_corner(
            base_glyph.getPen(),
            sx * self.thinning,
            sy,
            xe,
            (b.y1 + b.height * self.loop_ratio) / 2,
            b.xmid,
            b.y1,
            b.hx,
            b.hy * self.loop_ratio,
            orientation="bottom-right",
        )
        params = draw_arch(
            base_glyph.getPen(),
            sx,
            sy,
            b.x1,
            b.y1,
            b.x2,
            b.y1 + b.height * self.loop_ratio,
            b.hx,
            b.hy * self.loop_ratio,
            taper=self.taper * dc.taper,
            side="left",
            cut="bottom",
        )

        (x1, _), (x2, _) = params["inner"].intersection_y(y=yj)
        xj = min(x1, x2)

        # Remove the left-middle part
        cut_glyph = ufoLib2.objects.Glyph()
        ymid = b.y1 + b.height * self.loop_ratio / 2
        draw_rect(
            cut_glyph.getPen(),
            b.x1 - 10,
            2 * ymid - yj,
            b.xmid,
            yj,
        )

        result = BooleanGlyph(base_glyph).difference(BooleanGlyph(cut_glyph))
        result.draw(pen)

        theta, delta = draw_parallelogramm(
            NullPen(), sx, sy, xj, yj, xj + oj, b.y2, delta=sd
        )
        draw_parallelogramm(
            pen, sx, sy, xj - delta, yj, xj + oj - delta, b.y2, delta=sd
        )
        draw_rect(pen, xj + oj - 2 * delta, b.y2 - sy, xc, b.y2)
