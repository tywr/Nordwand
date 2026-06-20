from draw.rect import draw_rect
from glyphs.uppercase import UppercaseGlyph
from draw.arch import draw_arch


class UppercaseOeGlyph(UppercaseGlyph):
    # Placeholder: plots the same as uppercase 'A' for the moment.
    name = "uppercase_oe"
    unicode = "0x153"
    sbl = 0.622
    sbr = 0.598
    bar_height = 0.35
    overlap = 0.25
    stroke_x_ratio = 1.02
    width_ratio = 1.779
    mid_ratio = 0.52
    xmid_ratio = 0.55
    hx_ratio = 0.7
    bold_width_ratio = 1.648
    bold_sbl = 0.634
    bold_sbr = 0.563

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        ymid = self.mid_ratio * b.height
        xmid = b.x1 + self.xmid_ratio * b.width

        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1,
            xmid + sx / 2,
            b.y2,
            b.hx * self.hx_ratio,
            b.hy,
        )

        draw_rect(pen, xmid - sx / 2, b.y1, xmid + sx / 2, b.y2)

        # Vertical stem
        draw_rect(pen, xmid, ymid - sy / 2, b.x2, ymid + sy / 2)

        # Top bar
        draw_rect(pen, xmid, b.y2 - sy, b.x2, b.y2)

        # Middle bar
        draw_rect(
            pen,
            xmid,
            b.y1,
            b.x2,
            b.y1 + sy,
        )
