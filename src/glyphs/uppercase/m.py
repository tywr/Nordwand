from math import cos, sin
import ufoLib2
from booleanOperations.booleanGlyph import BooleanGlyph
from glyphs.uppercase import UppercaseGlyph
from draw.rect import draw_rect
from draw.parallelogramm import draw_parallelogramm_vertical
from draw.polygon import draw_polygon


class UppercaseMGlyph(UppercaseGlyph):
    name = "uppercase_m"
    unicode = "0x4D"
    overlap = 0.65
    overlap_middle = 0.5
    depth = 0.6
    inner_thickness_ratio = 2.4
    inner_height = 0.0
    width_ratio = 1.5

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="cap",
            width=dc.width * self.width_ratio + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            uppercase=True,
        )
        tsx = dc.stroke_x * self.stroke_x_ratio
        sx = max(0, 0.65 * (tsx - 90)) + min(90, tsx)
        delta = self.inner_thickness_ratio * sx
        yi = b.y1 + self.inner_height * b.height

        # Vertical stems

        glyph = ufoLib2.objects.Glyph()
        gpen = glyph.getPen()
        draw_rect(gpen, b.x1, b.y1, b.x1 + sx, b.y2)
        draw_rect(gpen, b.x2 - sx, b.y1, b.x2, b.y2)
        draw_parallelogramm_vertical(
            gpen,
            0,
            0,
            b.x1 + sx,
            b.y2,
            b.xmid,
            yi - delta / 2,
            direction="bottom-right",
            delta=delta,
        )
        theta, _ = draw_parallelogramm_vertical(
            gpen,
            0,
            0,
            b.x2 - sx,
            b.y2,
            b.xmid,
            yi - delta / 2,
            direction="bottom-left",
            delta=delta,
        )
        draw_rect(
            gpen,
            b.xmid,
            yi,
            b.xmid,
            yi + delta / 2,
        )
        draw_rect(
            gpen,
            b.x1 + sx,
            b.y2 - delta,
            b.x1 + sx,
            b.y2,
        )
        draw_rect(
            gpen,
            b.x2 - sx,
            b.y2 - delta,
            b.x2 - sx,
            b.y2,
        )
        cut_glyph = ufoLib2.objects.Glyph()
        draw_rect(
            cut_glyph.getPen(),
            b.x1 + sx,
            yi - delta / 2,
            b.x2 - sx,
            yi,
        )

        res = BooleanGlyph(glyph).difference(BooleanGlyph(cut_glyph))
        res.draw(pen)
