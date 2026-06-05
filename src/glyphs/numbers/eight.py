from glyphs.numbers import NumberGlyph
from draw.arch import draw_arch
from draw.rect import draw_rect


class EightGlyph(NumberGlyph):
    name = "eight"
    unicode = "0x38"
    height_ratio = 0.53
    loop_width_ratio = 0.92
    taper = 1.5
    extra_overshoot = 0.000
    width_ratio = 1.07
    sbl = 0.76
    sbr = 0.76

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            overshoot_bottom=True,
            overshoot_top=True,
            number=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio
        ymid = b.y1 + b.height * self.height_ratio
        wtop = self.loop_width_ratio * b.width
        dtop = (b.width - wtop) / 2
        ov = self.extra_overshoot * b.height

        # Top loop
        taper = max(self.taper * dc.taper, 0.65)
        top_params = draw_arch(
            pen,
            sx,
            sy,
            b.x1 + dtop,
            ymid - sy / 2,
            b.x2 - dtop,
            b.y2 + ov,
            b.hx,
            b.hy * (1 - self.height_ratio),
            taper=taper,
            side="bottom",
        )

        # Bottom loop
        draw_arch(
            pen,
            sx,
            sy,
            b.x1,
            b.y1 - ov,
            b.x2,
            ymid + sy / 2,
            b.hx,
            b.hy * self.height_ratio,
            taper=taper,
            side="top",
        )
