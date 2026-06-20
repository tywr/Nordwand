from glyphs import Glyph
from draw.rect import draw_rect


class RightSquareBracketGlyph(Glyph):
    name = "right_square_bracket"
    unicode = "0x5D"
    width_ratio = 0.350
    sbl = 0.585
    sbr = 0.939
    bold_width_ratio = 0.467
    bold_sbl = 0.254
    bold_sbr = 0.944

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
