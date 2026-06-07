from glyphs import Glyph
from draw.rect import draw_rect


class LeftSquareBracketGlyph(Glyph):
    name = "left_square_bracket"
    unicode = "0x5B"
    width_ratio = 0.6

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
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
