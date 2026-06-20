from glyphs.uppercase import UppercaseGlyph
from draw.loop import draw_loop
from draw.rect import draw_rect


class UppercaseOSlashGlyph(UppercaseGlyph):
    # Plots the same as uppercase 'O' for the moment (slash to be added later).
    name = "capital_oslash"
    unicode = "0xD8"
    sbl = 0.305
    sbr = 0.293
    stroke_x_ratio = UppercaseGlyph.stroke_x_ratio * 1.00
    stroke_y_ratio = UppercaseGlyph.stroke_y_ratio * 1.00
    width_ratio = 1.421
    slash_stroke = 1.2
    slash_length = 1.5
    overshoot_top = True
    overshoot_bottom = True
    bold_width_ratio = 1.537
    bold_sbl = 0.113
    bold_sbr = 0.099

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = self.stroke_x_ratio * dc.stroke_x, self.stroke_y_ratio * dc.stroke_y * self.stroke_y_ratio
        ss = sy * self.slash_length
        sl = self.slash_length * b.width
        draw_loop(
            pen,
            dc.stroke_x * self.stroke_x_ratio,
            dc.stroke_y * self.stroke_y_ratio,
            b.x1,
            b.y1,
            b.x2,
            b.y2,
            b.hx,
            b.hy,
        )
        draw_rect(
            pen,
            b.xmid - sl / 2,
            b.ymid - ss / 2,
            b.xmid + sl / 2,
            b.ymid + ss / 2,
            rotate=55,
        )
