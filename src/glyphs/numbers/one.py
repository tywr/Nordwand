from glyphs.numbers import NumberGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm_vertical


class OneGlyph(NumberGlyph):
    name = "one"
    unicode = "0x31"
    branch_height = 0.35
    width_ratio = 0.65
    sbl = 0.5
    sbr = 1.75

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            number=True,
        )
        sx, sy = dc.stroke_x * self.stroke_x_ratio, dc.stroke_y * self.stroke_y_ratio

        # Vertical stem (centered)
        draw_rect(pen, b.x2 - sx, b.y1, b.x2, b.y2)

        theta, delta = draw_parallelogramm_vertical(
            pen,
            sx,
            sy,
            b.x1,
            b.y1 + b.height * (1 - self.branch_height),
            b.x2 - sx,
            b.y2,
        )
