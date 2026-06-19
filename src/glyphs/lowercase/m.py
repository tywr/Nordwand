from glyphs import Glyph
from draw.arch import draw_arch
from draw.rect import draw_rect


class LowercaseMGlyph(Glyph):
    name = "lowercase_m"
    unicode = "0x6D"
    width_ratio = 1.477
    bold_width_ratio = 1.638
    mid_len = 1
    top_stroke_y = 1
    loop_ratio = 0.65
    hx_ratio = 0.5
    hy_ratio = 0.7
    right_hx_ratio = 0.8
    taper1 = 0.4
    taper2 = 0.6
    ending_thickness = 0.75
    min_width = 74
    sbl = 0.942
    sbr = 0.884
    overshoot_top = True
    bold_sbl = 0.936
    bold_sbr = 0.872

    def draw(self, pen, dc):
        b = self.body_bounds(dc)
        taper1 = self.taper1 * dc.taper
        taper2 = self.taper2 * dc.taper
        mid_y = (1 - self.mid_len) * (b.height - b.y1)
        hx, hy = b.hx * self.hx_ratio, self.hy_ratio * b.hy
        sx = dc.stroke_x
        ymid = b.y2 - 0.5 * b.height * self.loop_ratio

        wo = (b.width - 3 * sx) / 2
        if wo < self.min_width:
            smid = b.width - 2 * sx - 2 * self.min_width
        else:
            smid = sx
        mid_offset = smid / 2

        # Left arch (x1 to xmid) and store offset_x

        # glyph = ufoLib2.objects.Glyph()

        draw_arch(
            pen,
            smid,
            self.top_stroke_y * dc.stroke_y,
            b.x1 + (sx - smid),
            b.y2 - (b.height * self.loop_ratio),
            b.xmid + mid_offset,
            b.y2,
            hx,
            hy,
            taper=taper1,
            side="left",
            cut="bottom",
        )

        # Right arch (xmid to x2)
        draw_arch(
            pen,
            sx,
            self.top_stroke_y * dc.stroke_y,
            b.xmid - mid_offset - (sx - smid),
            b.y2 - (b.height * self.loop_ratio),
            b.x2,
            b.y2,
            hx,
            hy,
            taper=taper2,
            side="left",
            cut="bottom",
        )

        # Left stem
        draw_rect(pen, b.x1, 0, b.x1 + sx, dc.x_height)

        # Right foot — reaches up to the arch midpoint
        draw_rect(pen, b.x2 - sx, 0, b.x2, ymid)

        # Middle stem extension — extend past b.ymid into the arch so the
        # union is a clean polygon. Without this overlap, pathops sees the
        # arch's underside and the middle stem's top sharing an edge at
        # y=b.ymid and emits the shared edge as a boundary, producing a
        # stray horizontal stroke across the left counter in some weights.
        draw_rect(
            pen,
            b.xmid - smid / 2,
            mid_y,
            b.xmid + smid / 2,
            ymid + 1,
        )
