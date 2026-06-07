from glyphs import Glyph
from draw.rect import draw_rect
from draw.loop import draw_loop
from draw.polygon import draw_polygon


class QuestionMarkGlyph(Glyph):
    name = "question_mark"
    unicode = "0x3F"
    width_ratio = 1
    loop_ratio = 0.6
    hx_ratio = 1
    gap = 0.35
    dot_stroke_ratio = 1.1
    height_overflow = 0.05
    taper_length = 0.25
    taper = 0.75
    height = "cap"
    overshoot_top = True

    def draw(self, pen, dc):
        from glyphs.special.full_stop import FullStopGlyph

        b = self.body_bounds(dc)
        g = self.gap * b.height
        dh = self.height_overflow * b.height
        h = self.loop_ratio * b.height
        sd = dc.stroke_x * self.dot_stroke_ratio
        sx, sy = dc.stroke_x, dc.stroke_y
        hx = self.hx_ratio * b.hx
        draw_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y2 - h + dh,
            b.x2,
            b.y2 + dh,
            hx,
            b.hy * self.loop_ratio,
            cut="bottom",
        )
        draw_loop(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1,
            b.y2 - h + dh,
            b.x2,
            b.y2 + dh,
            hx,
            b.hy * self.loop_ratio,
            cut="left",
        )
        draw_rect(
            pen,
            b.xmid - dc.stroke_x / 2,
            b.y1 + g + h * self.taper_length,
            b.xmid + dc.stroke_x / 2,
            b.y2 - h + dh + sy,
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
