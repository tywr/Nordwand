from glyphs import Glyph
from draw.rect import draw_rect
from draw.loop import draw_loop
from draw.polygon import draw_polygon


class QuestionMarkGlyph(Glyph):
    name = "question_mark"
    unicode = "0x3F"
    loop_ratio = 0.55
    hx_ratio = 1
    gap = 0.3
    dot_stroke_ratio = 1.1
    taper_length = 0.2
    taper = 0.85
    height = "cap"
    overshoot_top = True
    width_ratio = 0.85
    sbl = 1.134
    sbr = 1.000
    bold_width_ratio = 0.9
    bold_sbl = 1.169
    bold_sbr = 0.817

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        g = self.gap * b.height
        h = self.loop_ratio * b.height
        sd = dc.stroke_x * self.dot_stroke_ratio
        sx, sy = dc.stroke_x, dc.stroke_y
        hx = self.hx_ratio * b.hx
        draw_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y2 - h,
            b.x2,
            b.y2,
            hx,
            b.hy * self.loop_ratio,
            cut="bottom",
        )
        draw_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y2 - h,
            b.x2,
            b.y2,
            hx,
            b.hy * self.loop_ratio,
            cut="left",
        )
        draw_rect(
            pen,
            b.xmid - dc.stroke_x / 2,
            b.y1 + g + h * self.taper_length,
            b.xmid + dc.stroke_x / 2,
            b.y2 - h + sy,
        )
        draw_polygon(
            pen,
            points=[
                (b.xmid + sx / 2, b.y1 + g + h * self.taper_length),
                (b.xmid - sx / 2, b.y1 + g + h * self.taper_length),
                (b.xmid - self.taper * sx / 2, b.y1 + g),
                (b.xmid + self.taper * sx / 2, b.y1 + g),
            ],
        )

        draw_rect(pen, b.xmid - sd / 2, 0, b.xmid + sd / 2, sd)
