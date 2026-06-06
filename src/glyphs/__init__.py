from abc import ABC, abstractmethod


class Glyph(ABC):
    accent_x_offset: int = 0
    sbl: int = 1
    sbr: int = 1
    stroke_x_ratio: float = 1

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def unicode(self) -> str: ...

    number_characters: int = 1
    font_feature: dict = None
    default_italic: bool = False

    def window_width(self, dc):
        return (
            self.width_ratio * dc.width
            + dc.default_stroke
            + (self.sbr + self.sbl) * dc.side_bearing
        )

    def diag_stroke_dampening(self, ratio, stroke, coef=0.25):
        from math import exp

        ds = max(stroke - 94, 0) / 94
        # If ds > 0, we add some dampening, other we let as is
        if ds <= 0:
            return ratio * stroke

        delta = exp(-ds * coef)
        sx = delta * stroke * ratio
        return sx

    @abstractmethod
    def draw(self, pen, dc) -> None: ...


class LigatureGlyph(Glyph):
    """Base class for ligature glyphs.

    Subclasses must define `components` — a list of glyph names that
    this ligature replaces (e.g. ["low_line", "low_line"] for "__").
    """

    unicode = None

    @property
    @abstractmethod
    def components(self) -> list[str]: ...


class ContextualLigatureGlyph(LigatureGlyph):
    """Ligature that only fires when not adjacent to `forbidden_neighbors`.

    Useful for capped-length ligatures: e.g. `==` and `===` ligate, but
    `====` and longer stay unligated. Set `forbidden_neighbors` to the
    glyph names whose presence on either side disqualifies the match
    (typically the ligature's own component glyph).
    """

    forbidden_neighbors: list[str] = []
