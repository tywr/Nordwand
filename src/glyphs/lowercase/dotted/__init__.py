from abc import ABC, abstractmethod
from glyphs import Glyph

from draw.rect import draw_rect


class DottedLowercaseGlyph(Glyph, ABC):
    """Define common class variables for single-story lowercase glyphs"""

    dot_height = 0.25
    dot_width = 1.1
    dot_position = "xmid"
    sbl = 1
    sbr = 1

    @abstractmethod
    def draw_base(self, pen, dc): ...

    def draw(self, pen, dc):
        self.draw_base(pen, dc)
        b = dc.body_bounds(
            width=self.width_ratio * dc.width + dc.stroke_x,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        w = dc.stroke_x * self.dot_width

        # Accent dot
        if self.dot_position == "x2":
            xpos = getattr(b, self.dot_position) - dc.stroke_x / 2
        elif self.dot_position == "x1":
            xpos = getattr(b, self.dot_position) + dc.stroke_x / 2
        else:
            xpos = getattr(b, self.dot_position)
        dh = self.dot_height * b.height
        draw_rect(
            pen,
            xpos - w / 2,
            dc.cap - dh,
            xpos + w / 2,
            dc.cap,
        )
