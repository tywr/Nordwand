from glyphs import LigatureGlyph
from draw.parallelogramm import draw_parallelogramm_vertical
from draw.rect import draw_rect


class RightArrowGlyph(LigatureGlyph):
    """Ligature glyph for ->"""

    name = "right_arrow"
    components = ["hyphen_minus", "greater_than_sign"]
    number_characters = 2
    width_ratio = 0.88
    overlap = 0.6
    span = 0.85
    stroke_ratio = 1.2

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="x_height",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        o = ((1 - self.width_ratio) * b.width) / 2
        ymid = dc.math
        h = dc.parenthesis_length * self.span
        s = dc.stroke_x
        s2 = self.stroke_ratio * dc.stroke_x
        draw_parallelogramm_vertical(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x2 + dc.window_width,
            ymid - s2 / 2,
            b.x1 + dc.window_width,
            ymid + h / 2,
            direction="top-left",
            delta=s2,
        )
        draw_parallelogramm_vertical(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.x1 + dc.window_width,
            ymid - h / 2,
            b.x2 + dc.window_width,
            ymid + s2 / 2,
            direction="top-right",
            delta=s2,
        )
        draw_rect(
            pen,
            b.x1 + o,
            dc.math - s / 2,
            b.x2 + dc.window_width,
            dc.math + s / 2,
        )
