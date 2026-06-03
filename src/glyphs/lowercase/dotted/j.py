from draw.square_corner import draw_square_corner
from draw.rect import draw_rect
from glyphs.lowercase.dotted import DottedLowercaseGlyph


class LowercaseJGlyph(DottedLowercaseGlyph):
    name = "lowercase_j"
    unicode = "0x6A"
    tail_offset = 0
    width_ratio = 0.25
    dot_position = "x2"
    sbl = -0.6
    sbr = 1

    def draw_base(self, pen, dc):
        """Draw the letter without the dot (for use with accents)."""
        b = dc.body_bounds(
            width=self.width_ratio * dc.width + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        x2 = b.x2
        # Stem
        draw_rect(pen, x2 - dc.stroke_x, 0, x2, dc.x_height)
        # Corner curving down-left into the descender
        draw_square_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            x2,
            0,
            b.x1,
            dc.descent + self.tail_offset,
            # dc.hx * 0.5,
            # dc.hy,
            orientation="bottom-left",
        )
