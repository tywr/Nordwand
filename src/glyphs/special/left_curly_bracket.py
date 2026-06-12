from glyphs import Glyph
from draw.rect import draw_rect
from draw.corner import draw_corner
from draw.square_corner import draw_square_corner


class LeftCurlyBracketGlyph(Glyph):
    name = "left_curly_bracket"
    unicode = "0x7B"
    peak_ratio = 0.0
    protusion_stroke_ratio = 1.3
    width_ratio = 0.626
    sbl = 0.465
    sbr = 0.465
    bold_width_ratio = 0.738
    bold_sbl = 0.468
    bold_sbr = 0.462

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        pl = self.peak_ratio * b.width
        ymid = dc.parenthesis
        sx, sy = dc.stroke_x, dc.stroke_y
        sp = dc.stroke_y * self.protusion_stroke_ratio
        y1, y2 = ymid - dc.parenthesis_length / 2, ymid + dc.parenthesis_length / 2
        x1, x2, xmid = b.x1 + pl, b.x2, (b.x1 + pl + b.x2) / 2
        l4 = dc.parenthesis_length / 4
        hx = (1 - self.peak_ratio) * b.hx
        hy = b.hy

        draw_square_corner(
            pen,
            sx,
            sy,
            xmid - sx / 2,
            y2 - l4,
            x2,
            y2,
            # hx,
            # hy,
            orientation="top-right",
        )
        draw_corner(
            pen,
            sx,
            0.75 * sp,
            xmid + sx / 2,
            y2 - l4,
            x1,
            ymid - 0.25 * sp,
            hx,
            hy,
            orientation="bottom-left",
        )

        draw_square_corner(
            pen,
            sx,
            sy,
            xmid - sx / 2,
            y1 + l4,
            x2,
            y1,
            # hx,
            # hy,
            orientation="bottom-right",
        )
        draw_corner(
            pen,
            sx,
            0.75 * sp,
            xmid + sx / 2,
            y1 + l4,
            x1,
            ymid + 0.25 * sp,
            hx,
            hy,
            orientation="top-left",
        )
