from glyphs import Glyph
from draw.polygon import draw_polygon


class CommaGlyph(Glyph):
    name = "comma"
    unicode = "0x2C"
    width_ratio = 0.5
    height_ratio = 0.75
    vertical_offset = 0.25
    foot_offset = 0.15
    taper = 0.5
    stroke_ratio = 1.15
    sbl = -0.25
    sbr = 1

    def draw(self, pen, dc):
        b = dc.body_bounds(
            height="x_height",
            width=dc.width * self.width_ratio + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        h = self.height_ratio * b.height
        sx = self.stroke_ratio * dc.stroke_x
        oy = self.vertical_offset * b.height
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
