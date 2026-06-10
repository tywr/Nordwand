import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs import Glyph
from draw.square_corner import draw_square_corner
from draw.rect import draw_rect
from draw.polygon import draw_polygon


class LowercaseTGlyph(Glyph):
    name = "lowercase_t"
    unicode = "0x74"
    width_ratio = 0.590
    bold_width_ratio = 0.68
    rl_ratio = 0.445
    up_ratio = 0.32
    angle_offset = 0.3
    sbl = 0.349
    sbr = 0.570

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        xmid = b.x1 * (1 - self.rl_ratio) + b.x2 * self.rl_ratio
        ao = self.angle_offset * b.width

        # Cross-bar at x_height
        draw_rect(
            pen,
            b.x1,
            dc.x_height - dc.stroke_y,
            b.x2,
            dc.x_height,
        )
        # Corner curving down-right (shorter/flatter than f)
        draw_square_corner(
            pen,
            dc.stroke_x,
            dc.stroke_y,
            xmid - dc.stroke_x / 2,
            b.ymid,
            b.x2,
            0,
            orientation="bottom-right",
        )
        # Footer extension from corner to right edge
        draw_rect(
            pen,
            b.xmid + b.width / 2,
            0,
            b.x2,
            dc.stroke_y,
        )

        glyph = ufoLib2.objects.Glyph()

        # Stem
        draw_rect(
            glyph.getPen(),
            xmid - dc.stroke_x / 2,
            b.ymid,
            xmid + dc.stroke_x / 2,
            (1 + self.up_ratio) * dc.x_height,
        )
        cut_glyph = ufoLib2.objects.Glyph()

        draw_polygon(
            cut_glyph.getPen(),
            points=[
                (xmid + dc.stroke_x / 2, (1 + self.up_ratio) * dc.x_height),
                (
                    b.x1 - ao,
                    dc.x_height,
                ),
                (
                    b.x1 - ao,
                    (1 + self.up_ratio) * dc.x_height,
                ),
            ],
        )
        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
