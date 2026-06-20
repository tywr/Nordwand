from glyphs import Glyph
from draw.rect import draw_rect


class SemiColonGlyph(Glyph):
    name = "semi_colon"
    unicode = "0x3B"
    sbl = 0.646
    sbr = 0.951
    width_ratio = 0.320
    bold_width_ratio = 0.387
    stroke_ratio = 1.2
    stroke_ratio_bold = 1
    gap = 0.935
    bold_sbl = 0.535
    bold_sbr = 0.901

    def draw(self, pen, dc):
        from glyphs.special.comma import CommaGlyph

        b = self.body_bounds(dc)
        bw = max(0, dc.weight - 400) / 300
        sr = (1 - bw) * self.stroke_ratio + bw * self.stroke_ratio_bold
        s = sr * dc.stroke_x
        g = b.height * self.gap

        draw_rect(
            pen,
            b.xmid - s / 2,
            b.y1 + g - s,
            b.xmid + s / 2,
            b.y1 + g,
        )
        cg = CommaGlyph()
        cg.draw(pen, dc)
