from glyphs import Glyph
from draw.square_corner import draw_square_corner
from draw.rect import draw_rect


class LowercaseFGlyph(Glyph):
    name = "lowercase_f"
    unicode = "0x66"
    rl_ratio = 0.53
    cross_bar_height = 1
    right_bar_offset = 0.018
    width_ratio = 0.624
    bold_width_ratio = 0.670
    thickening = 1.1
    sbl = 0.195
    sbr = 0.183
    bold_sbl = 0.197
    bold_sbr = 0.113

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        yc = self.cross_bar_height * dc.x_height
        xmid = b.x1 * self.rl_ratio + b.x2 * (1 - self.rl_ratio)
        x2 = b.x2 - self.right_bar_offset * b.width

        # Stem
        draw_rect(pen, xmid - dc.stroke_x / 2, 0, xmid + dc.stroke_x / 2, dc.x_height)

        # Cross-bar
        draw_rect(
            pen,
            b.x1,
            yc - dc.stroke_y,
            x2,
            yc,
        )

        # Corner
        draw_square_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y * self.thickening,
            xmid - dc.stroke_x / 2,
            dc.x_height,
            b.x2,
            dc.ascent,
            orientation="top-right",
        )
