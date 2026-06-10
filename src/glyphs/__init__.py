from abc import ABC, abstractmethod


class Glyph(ABC):
    width_ratio: float = 1
    bold_width_ratio: float = 1
    accent_x_offset: int = 0
    sbl: int = 1
    sbr: int = 1
    stroke_x_ratio: float = 1
    overshoot_top: bool = False
    overshoot_bottom: bool = False
    height: str = "x_height"
    number: bool = False
    uppercase: bool = False

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def unicode(self) -> str: ...

    number_characters: int = 1
    font_feature: dict = None
    default_italic: bool = False

    def extra_cut(self, dc):
        if self.uppercase:
            return 0.6 * max(0, dc.stroke_x - dc.default_stroke)
        else:
            return 0.35 * max(0, dc.stroke_x - dc.default_stroke)

    def adjusted_width_ratio(self, dc):
        if dc.weight <= 400:
            width_ratio = self.width_ratio
        elif dc.weight <= 700:
            bw = (dc.weight - 400) / 300
            width_ratio = (1 - bw) * self.width_ratio + bw * self.bold_width_ratio
        return width_ratio

    def window_width(self, dc):
        return (
            self.adjusted_width_ratio(dc) * dc.width
            + (self.sbr + self.sbl) * dc.side_bearing
        )

    def diag_stroke_dampening(self, ratio, stroke, coef=0.25):
        from math import exp

        ds = max(stroke - 85, 0) / 85
        # If ds > 0, we add some dampening, other we let as is
        if ds <= 0:
            return ratio * stroke

        delta = exp(-ds * coef)
        sx = delta * stroke * ratio
        return sx

    def body_bounds(self, dc):
        return dc.body_bounds(
            width=self.adjusted_width_ratio(dc) * dc.width,
            side_bearing_right=self.sbr * dc.side_bearing,
            side_bearing_left=self.sbl * dc.side_bearing,
            height=self.height,
            number=self.number,
            uppercase=self.uppercase,
            overshoot_bottom=self.overshoot_bottom,
            overshoot_top=self.overshoot_top,
        )

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
