from glyphs import Glyph
from draw.rect import draw_rect


class LeftSquareBracketGlyph(Glyph):
    name = "left_square_bracket"
    unicode = "0x5B"
    width_ratio = 0.6

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="x_height",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        ymid = dc.parenthesis
        
        draw_rect(
            pen,
            b.x1,
            ymid - dc.parenthesis_length / 2,
            b.x1 + dc.stroke_x,
            ymid + dc.parenthesis_length / 2,
        )
        draw_rect(
            pen,
            b.x1,
            ymid + dc.parenthesis_length / 2 - dc.stroke_y,
            b.x2,
            ymid + dc.parenthesis_length / 2,
        )
        draw_rect(
            pen,
            b.x1,
            ymid - dc.parenthesis_length / 2,
            b.x2,
            ymid - dc.parenthesis_length / 2 + dc.stroke_y,
        )
