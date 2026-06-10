from glyphs import Glyph
from draw.rect import draw_rect


class RightSquareBracketGlyph(Glyph):
    name = "right_square_bracket"
    unicode = "0x5D"
    width_ratio = 0.6
    bold_width_ratio = 0.558
    bold_sbl = 0.468
    bold_sbr = 1.609

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        ymid = dc.parenthesis

        draw_rect(
            pen,
            b.x2 - dc.stroke_x,
            ymid - dc.parenthesis_length / 2,
            b.x2,
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
