from glyphs import Glyph
from draw.smooth_corner import draw_smooth_corner
from draw.rect import draw_rect


class LowercaseF2Glyph(Glyph):
    name = "lowercase_f_2"
    unicode = "0x66"
    font_feature = {"ss02": 1}
    default_italic = True
    rl_ratio = 0.55
    width_ratio = 1.25

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="x_height",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        right_len = b.width * self.rl_ratio - dc.stroke_x / 2
        left_len = b.width * (1 - self.rl_ratio) - dc.stroke_x / 2

        # Stem
        draw_rect(
            pen,
            b.xmid - dc.stroke_x / 2,
            dc.descent,
            b.xmid + dc.stroke_x / 2,
            dc.x_height,
        )
        # Cross-bar
        draw_rect(
            pen,
            b.xmid - left_len - dc.stroke_x / 2,
            dc.x_height - dc.stroke_y,
            b.xmid + right_len + dc.stroke_x / 2,
            dc.x_height,
        )
        # Corner
        draw_smooth_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            b.xmid - dc.stroke_x / 2,
            dc.x_height,
            b.xmid + right_len + dc.stroke_x / 2,
            dc.ascent,
            right_len + dc.stroke_x,
            dc.ascent - dc.x_height,
            orientation="top-right",
        )
