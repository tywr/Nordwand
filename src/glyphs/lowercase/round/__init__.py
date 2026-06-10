from abc import ABC
from glyphs import Glyph


class RoundLowercaseGlyph(Glyph, ABC):
    """Define common class variables for round lowercase glyphs"""

    overshoot_top = True
    overshoot_bottom = True

    stroke_x_ratio = 1.01
    stroke_y_ratio = 1.06

    hy_ratio = 1
    hx_ratio = 1

    sbl = 0.628
    sbr = 0.628
