import dataclasses
from dataclasses import dataclass
from utils.bounds import BodyBounds
from kerning import KERNING_TABLE


@dataclass
class FontConfig:
    """Default metrics used for the project, can be overwritten with a yaml file"""

    family_name: str = "Nordwand"

    units_per_em: int = 1000
    window_ascent: int = 1025
    window_descent: int = -300
    window_width: int = 600

    ascent: int = 735
    descent: int = -175
    cap: int = 705
    x_height: int = 526

    accent: int = 715
    accent_cap: int = 890

    math: int = 300

    parenthesis: int = 300
    parenthesis_length: int = 1060

    min_margin_lowercase: int = 26
    min_margin_uppercase: int = 40

    italic_angle: float = 9.4

    space = 280
    side_bearing = 84

    hx: int = 152
    hy: int = 187

    cap_hx: int = 140
    cap_hy: int = 180

    taper: float = 0.58

    width: int = 398
    default_stroke: int = 85
    stroke_x: int = 85
    stroke_y: int = 64
    stroke_alt: int = 64

    # width: int = 398
    # default_stroke: int = 85
    # stroke_x = 85
    # stroke_y = 70
    # stroke_alt = 70

    v_overshoot: int = 9
    v_overshoot_cap: int = 16
    h_overshoot: int = 10

    # Kerning pairs: {"<char1><char2>": fraction_of_side_bearing}.
    # e.g. {"vo": -0.5} shifts "o" left by 0.5 * side_bearing units after "v".
    # Plain class attribute (not a dataclass field) so the YAML overlay and the
    # __init__ defaults rebuild in apply_config_overrides leave it untouched.
    kerning = KERNING_TABLE


@dataclass
class DrawConfig(FontConfig):
    # Can be overwritten for bold / thinner fonts
    x_height: int = FontConfig.x_height
    cap: int = FontConfig.cap
    ascent: int = FontConfig.ascent
    descent: int = FontConfig.descent
    accent: int = FontConfig.accent
    accent_cap: int = FontConfig.accent_cap
    width: int = FontConfig.width
    side_bearing: int = FontConfig.side_bearing
    hx: int = FontConfig.hx
    hy: int = FontConfig.hy
    cap_hx: int = FontConfig.cap_hx
    cap_hy: int = FontConfig.cap_hy
    taper: int = FontConfig.taper
    default_stroke: int = FontConfig.default_stroke
    stroke_x: int = FontConfig.stroke_x
    stroke_y: int = FontConfig.stroke_y
    stroke_alt: int = FontConfig.stroke_alt
    v_overshoot: int = FontConfig.v_overshoot
    v_overshoot_cap: int = FontConfig.v_overshoot_cap
    h_overshoot: int = FontConfig.h_overshoot

    italic: bool = False

    @classmethod
    def weight(cls, w=400):
        """Return a DrawConfig with heavier stroke weights for a bold variant."""
        from math import log, exp

        brx = 1.7
        ratio_x = exp((w - 400) * log(brx) / 300)

        bry = 1.4
        ratio_y = exp((w - 400) * log(bry) / 300)

        bhy = 1.3
        hy_ratio = exp((w - 400) * log(bhy) / 300)

        # Function mapping 100 → 0.5 and 700 → 0.2
        taper = min(0.5, 0.5 - 0.0009 * (w - 400))

        ds = cls.stroke_x * (ratio_x - 1) + cls.default_stroke
        extra_sb = max(cls.stroke_x * ratio_x - cls.default_stroke, 0) / 4
        return cls(
            default_stroke=int(ds),
            width=int(cls.width),
            stroke_x=int(cls.stroke_x * ratio_x),
            stroke_y=int(cls.stroke_y * ratio_y),
            stroke_alt=int(cls.stroke_alt * ratio_y),
            side_bearing=cls.side_bearing + extra_sb,
            x_height=cls.x_height,
            cap=cls.cap,
            accent=cls.cap,
            accent_cap=cls.accent_cap,
            ascent=cls.ascent,
            descent=cls.descent,
            taper=taper,
            hy=hy_ratio * cls.hy,
            cap_hy=hy_ratio * cls.cap_hy,
        )

    @classmethod
    def for_italic(cls):
        return cls(
            stroke_x=int(cls.stroke_x),
            stroke_y=int(cls.stroke_y),
            stroke_alt=int(cls.stroke_alt),
            taper=cls.taper,
            italic=True,
        )

    def body_bounds(
        self,
        width=1,
        side_bearing_right=0,
        side_bearing_left=0,
        height="x_height",
        overshoot_top=False,
        overshoot_bottom=False,
        number=False,
        uppercase=False,
    ):
        """
        Abstraction for storing common metrics relative to the body
        of a character. For most lowercase, the boundaries are
        a centered rectangle of length `width` and of height `x-height`.
        For most capital letters, it's a centered rectangle of length
        `width` and height `ascent`.
        """
        if height not in ["x_height", "ascent", "cap"]:
            raise ValueError(f"Value {height} should be `x_height`, `ascent` or `cap`")
        y1 = 0
        x1 = side_bearing_left
        x2 = x1 + width
        y2 = getattr(self, height)

        if uppercase:
            v_ov = self.v_overshoot_cap
        else:
            v_ov = self.v_overshoot
        h_ov = self.h_overshoot

        if overshoot_bottom:
            y1 -= v_ov
        if overshoot_top:
            y2 += v_ov

        # Rescale the hx and hy for the new box
        if uppercase:
            hx = self.cap_hx
            hy = self.cap_hy
        else:
            hx = self.hx
            hy = self.hy

        hx = hx * (x2 - x1 - self.stroke_x) / self.width
        hy = hy * (y2 - y1 - self.stroke_y) / self.x_height

        return BodyBounds(
            x1=x1, y1=y1, x2=x2, y2=y2, hx=hx, hy=hy, v_ov=v_ov, h_ov=h_ov
        )


def config_keys():
    """Names of all overridable configuration values."""
    keys = {f.name for f in dataclasses.fields(DrawConfig)}
    # `default_stroke` and `kerning` are plain class attributes (no annotation),
    # not dataclass fields.
    keys.add("default_stroke")
    keys.add("kerning")
    return keys


def kern_value(frac, dc):
    """Convert a kerning fraction into font units (fraction of side_bearing)."""
    return round(frac * dc.side_bearing)


def apply_config_overrides(overrides):
    """Overwrite the default FontConfig / DrawConfig values in place.

    `overrides` is a mapping of config name -> value. The values are written
    onto both classes so that:
      * static access (`fc.window_width`, `fc.accent`, ...) sees them, and
      * instantiation (`DrawConfig()`, `.weight()`, `.for_italic()`) sees them,
        which requires rebuilding the dataclass `__init__` defaults.

    Raises ValueError on unknown keys so typos fail loudly.
    """
    valid = config_keys()
    unknown = set(overrides) - valid
    if unknown:
        raise ValueError(
            f"Unknown config keys: {sorted(unknown)}. Valid keys: {sorted(valid)}"
        )

    for key, value in overrides.items():
        for cls in (FontConfig, DrawConfig):
            if hasattr(cls, key):
                setattr(cls, key, value)

    # Reassigning a class attribute does not change the dataclass `__init__`
    # default (which is baked in at class creation), so rebuild it from the
    # current class attributes, in field order.
    DrawConfig.__init__.__defaults__ = tuple(
        getattr(DrawConfig, f.name) for f in dataclasses.fields(DrawConfig)
    )

    return overrides


def load_config(path):
    """Load a YAML file and apply it as overrides to the font configuration.

    Returns the dict of applied overrides.
    """
    import yaml

    with open(path) as fh:
        data = yaml.safe_load(fh) or {}
    if not isinstance(data, dict):
        raise ValueError(
            f"Config file {path!r} must contain a top-level mapping of "
            f"config name -> value"
        )
    return apply_config_overrides(data)
