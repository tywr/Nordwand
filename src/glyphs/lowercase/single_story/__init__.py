from abc import ABC
from glyphs import Glyph


class SingleStoryLowercaseGlyph(Glyph, ABC):
    """Define common class variables for single-story lowercase glyphs"""

    taper = 0.8
    width_ratio = 0.97
    sbl = 1
    sbr = 1

    ending_thickness = 0.8

    bowl_stroke_x_ratio = 1.01
    bowl_stroke_y_ratio = 1.00

    hx_ratio = 1.03
    hy_ratio = 1

    def window_width(self, dc):
        return self.width_ratio * dc.width + dc.stroke_x + (self.sbr + self.sbl) * dc.side_bearing
