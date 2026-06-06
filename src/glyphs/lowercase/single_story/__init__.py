from abc import ABC
from glyphs import Glyph


class SingleStoryLowercaseGlyph(Glyph, ABC):
    """Define common class variables for single-story lowercase glyphs"""

    taper = 0.8
    width_ratio = 0.98
    sbl = 1
    sbr = 1

    ending_thickness = 0.8

    bowl_stroke_x_ratio = 1.01
    bowl_stroke_y_ratio = 1.00

    hx_ratio = 1.0
    hy_ratio = 1
