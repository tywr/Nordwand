from glyphs import Glyph
from draw.polygon import draw_polygon


class CommaGlyph(Glyph):
    name = "comma"
    unicode = "0x2C"
    width_ratio = 0.320
    bold_width_ratio = 0.387
    height_ratio = 0.7
    vertical_offset = 0.19
    foot_offset = 0.15
    taper = 0.35
    stroke_ratio = 1.05
    sbl = 0.646
    sbr = 0.951
    bold_sbl = 0.507
    bold_sbr = 0.930

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        ec = self.extra_cut(dc)
        h = self.height_ratio * b.height + 4 * ec
        sx = self.stroke_ratio * dc.stroke_x
        oy = self.vertical_offset * b.height + ec
        fx = self.foot_offset * b.width

        draw_polygon(
            pen,
            points=[
                (b.xmid - sx / 2, oy),
                (b.xmid + sx / 2, oy),
                (b.xmid + self.taper * sx / 2 - fx, oy - (h - sx)),
                (b.xmid - sx / 2 - fx, oy - h + sx),
            ],
        )
