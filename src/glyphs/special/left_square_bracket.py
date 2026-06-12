from glyphs import Glyph
from draw.rect import draw_rect


class LeftSquareBracketGlyph(Glyph):
    name = "left_square_bracket"
    unicode = "0x5B"
    width_ratio = 0.437
    sbl = 1.558
    sbr = 0.465
    bold_width_ratio = 0.558
    bold_sbl = 1.615
    bold_sbr = 0.462

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
