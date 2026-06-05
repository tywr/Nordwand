from abc import ABC, abstractmethod
from glyphs import Glyph


class Accent(Glyph, ABC):
    """Base class for accent/diacritical marks.

    Accents are full glyphs (can be visualized standalone) and also
    provide draw_at(pen, dc, x, y) for positioning by ComposedGlyph.
    """

    width_ratio = 1

    @abstractmethod
    def draw_at(self, pen, dc, x, y):
        """Draw the accent centered horizontally at x, vertically at y."""
        ...

    def draw(self, pen, dc):
        """Draw the accent at the default position (centered in the cell)."""
        b = dc.body_bounds(
            width=dc.width * self.width_ratio + dc.stroke_x * self.stroke_x_ratio,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
        )
        self.draw_at(pen, dc, x=b.xmid, y=dc.accent)
