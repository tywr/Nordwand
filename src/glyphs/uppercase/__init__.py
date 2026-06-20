from abc import ABC
from glyphs import Glyph


class UppercaseGlyph(Glyph, ABC):
    """Define common class variables for all uppercase glyphs"""

    width_ratio = 1.00
    bold_width_ratio = 1.2
    stroke_x_ratio = 1.075
    stroke_y_ratio = 1.22

    height = "cap"
    uppercase = True
