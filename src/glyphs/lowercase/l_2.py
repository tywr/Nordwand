from glyphs import Glyph
from draw.rect import draw_rect


class LowercaseL2Glyph(Glyph):
    name = "lowercase_l_2"
    unicode = "0x6C"
    font_feature = {"cv03": 1}
    width_ratio = 1.08
    cap = 0.45

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="ascent",
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        right_len = 0.5 * b.width - dc.stroke_x / 2
        left_len = 0.5 * b.width - dc.stroke_x / 2

        # Stem
        draw_rect(pen, b.xmid - dc.stroke_x / 2, 0, b.xmid + dc.stroke_x / 2, dc.ascent)

        # Footer
        draw_rect(
            pen,
            b.xmid - left_len - dc.stroke_x / 2,
            0,
            b.xmid + right_len + dc.stroke_x / 2,
            dc.stroke_y,
        )
        # Left cap
        draw_rect(
            pen,
            b.xmid - b.width * self.cap,
            dc.ascent - dc.stroke_y,
            b.xmid,
            dc.ascent,
        )
