from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm


class UppercaseMGlyph(UppercaseGlyph):
    name = "uppercase_m"
    unicode = "0x4D"
    overlap = 0.65
    overlap_middle = 0.5
    depth = 0.6
    inner_thickness_ratio = 1
    inner_height = 0.0
    width_ratio = 1.431
    bold_width_ratio = 1.517
    overlap = 0.1
    sbr = 1.070
    sbl = 1.070
    bold_sbl = 1.122
    bold_sbr = 1.122

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        tsx = dc.stroke_x * self.stroke_x_ratio
        sx = max(0, 0.65 * (tsx - 90)) + min(90, tsx)
        delta = self.inner_thickness_ratio * sx
        ov = self.overlap * sx

        # Vertical stems
        draw_rect(pen, b.x1, b.y1, b.x1 + sx, b.y2)
        draw_rect(pen, b.x2 - sx, b.y1, b.x2, b.y2)
        draw_parallelogramm(
            pen,
            0,
            0,
            b.x1 + ov,
            b.y2,
            b.xmid + delta / 2,
            b.y1,
            direction="bottom-right",
            delta=delta,
        )
        theta, _ = draw_parallelogramm(
            pen,
            0,
            0,
            b.x2 - ov,
            b.y2,
            b.xmid - delta / 2,
            b.y1,
            direction="bottom-left",
            delta=delta,
        )
