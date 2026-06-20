import dataclasses
from dataclasses import dataclass
from utils.bounds import BodyBounds
from kerning import KERNING_TABLE
from kerning_bold import BOLD_KERNING_TABLE


@dataclass
class FontConfig:
    """Default metrics used for the project, can be overwritten with a yaml file"""

    family_name: str = "Nordwand"
    weight: int = 400

    units_per_em: int = 1000
    window_ascent: int = 1025
    window_descent: int = -300
    window_width: int = 600
    extra_window_width: int = 0

    ascent: int = 725
    descent: int = -190
    cap: int = 725
    x_height: int = 507

    accent: int = 685
    accent_cap: int = 890

    min_margin_lowercase: int = 26
    min_margin_uppercase: int = 40

    italic_angle: float = 9.4

    space = 290
    side_bearing = 82

    hx: int = 185
    hy: int = 170

    cap_hx: int = 190
    cap_hy: int = 160

    taper: float = 0.6

    # Classic config
    # width: int = 485
    # default_stroke: int = 85
    # stroke_x: int = 85
    # stroke_y: int = 71
    # stroke_alt: int = 71

    # Univers-like config
    width: int = 497
    default_stroke: int = 88
    stroke_x = 88
    stroke_y = 62
    stroke_alt = 62

    v_overshoot: int = 9
    v_overshoot_cap: int = 16
    v_overshoot_number: int = 13
    h_overshoot: int = 10

    # Kerning pairs: {"<char1><char2>": fraction_of_side_bearing}.
    # e.g. {"vo": -0.5} shifts "o" left by 0.5 * side_bearing units after "v".
    # Plain class attribute (not a dataclass field) so the YAML overlay and the
    # __init__ defaults rebuild in apply_config_overrides leave it untouched.
    # `kerning` is the regular (weight 400) table; `bold_kerning` is the weight
    # 700 table. For intermediate weights the two are linearly interpolated
    # (see `kerning_for_weight`).
    kerning = KERNING_TABLE
    bold_kerning = BOLD_KERNING_TABLE


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
    extra_window_width: int = FontConfig.extra_window_width

    math: int = 282

    parenthesis: int = (ascent + descent) / 2
    parenthesis_length: int = ascent - descent

    italic: bool = False

    @classmethod
    def weight(cls, w=400):
        """Return a DrawConfig with heavier stroke weights for a bold variant."""
        from math import log, exp

        # 166
        brx = 1.66
        ratio_x = exp((w - 400) * log(brx) / 300)

        # 97
        bry = 1.6
        ratio_y = exp((w - 400) * log(bry) / 300)

        bra = 1.2
        ratio_a = exp((w - 400) * log(bra) / 300)

        bhx = 1.15
        hx_ratio = exp((w - 400) * log(bhx) / 300)

        bhy = 1.1
        hy_ratio = exp((w - 400) * log(bhy) / 300)

        rb = 0.87
        sb_ratio = exp((w - 400) * log(rb) / 300)

        ro = 6
        exo = exp((w - 400) * log(ro) / 300)

        bt = 0.7
        ratio_taper = exp((w - 400) * log(bt) / 300)

        return cls(
            weight=w,
            stroke_x=cls.stroke_x * ratio_x,
            stroke_y=cls.stroke_y * ratio_y,
            stroke_alt=cls.stroke_alt * ratio_a,
            side_bearing=cls.side_bearing * sb_ratio,
            x_height=cls.x_height,
            cap=cls.cap,
            accent=cls.cap,
            accent_cap=cls.accent_cap,
            ascent=cls.ascent,
            descent=cls.descent,
            taper=cls.taper * ratio_taper,
            hx=hx_ratio * cls.hx,
            hy=hy_ratio * cls.hy,
            cap_hx=hx_ratio * cls.cap_hx,
            cap_hy=hy_ratio * cls.cap_hy,
            v_overshoot=cls.v_overshoot + exo,
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
        elif number:
            v_ov = self.v_overshoot_number
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
    keys.add("bold_kerning")
    return keys


def kern_value(frac, dc):
    """Convert a kerning fraction into font units (fraction of side_bearing)."""
    return round(frac * dc.side_bearing)


def kerning_for_weight(weight, base=None, bold=None):
    """Return the kerning table for `weight`, interpolating 400 -> 700.

    At weight 400 the regular `kerning` table is used, at 700 the
    `bold_kerning` table. For weights in between each pair's fraction is a
    linear blend of the two; a pair absent from a table counts as 0. Weights
    outside [400, 700] are clamped.
    """
    base = FontConfig.kerning if base is None else base
    bold = FontConfig.bold_kerning if bold is None else bold

    t = (max(400, min(700, weight)) - 400) / 300
    if t == 0:
        return dict(base)
    if t == 1:
        return dict(bold)

    return {
        pair: base.get(pair, 0.0) * (1 - t) + bold.get(pair, 0.0) * t
        for pair in set(base) | set(bold)
    }


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
