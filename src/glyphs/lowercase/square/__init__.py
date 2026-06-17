from abc import ABC
from glyphs import Glyph


class SquareLowercaseGlyph(Glyph, ABC):
    """Define common class variables for all squared lowercase glyphs"""

    hx_ratio = 1.3
    taper = 0.4
    width_ratio = 0.886
    ending_thickness = 0.8
    loop_ratio = 0.9

    sbr = 1
    sbl = 1
