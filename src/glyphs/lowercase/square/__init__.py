from abc import ABC
from glyphs import Glyph


class SquareLowercaseGlyph(Glyph, ABC):
    """Define common class variables for all squared lowercase glyphs"""

    hx_ratio = 1.0
    hy_ratio = 0.7
    taper = 0.55
    width_ratio = 0.886
    ending_thickness = 0.8
    loop_ratio = 0.65

    sbr = 1
    sbl = 1
