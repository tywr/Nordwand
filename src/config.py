import dataclasses
from dataclasses import dataclass
from utils.bounds import BodyBounds


@dataclass
class FontConfig:
    """Default metrics used for the project, can be overwritten with a yaml file"""

    family_name: str = "Nordwand"

    units_per_em: int = 1000
    window_ascent: int = 1025
    window_descent: int = -300
    window_width: int = 600

    ascent: int = 750
    descent: int = -200
    cap: int = 750
    x_height: int = 530

    accent: int = 715
    accent_cap: int = 890

    math: int = 300

    parenthesis: int = 300
    parenthesis_length: int = 1060

    min_margin_lowercase: int = 26
    min_margin_uppercase: int = 40

    default_stroke = 90
    italic_angle: float = 9.4

    space = 240
    width: int = 400
    side_bearing = 68

    hx: int = 180
    hy: int = 180

    cap_hx: int = 180
    cap_hy: int = 170

    taper: float = 0.5

    stroke_x: int = 94
    stroke_y: int = 66
    stroke_alt: int = 60

    v_overshoot: int = 12
    h_overshoot: int = 11

    # Kerning pairs: {"<char1><char2>": fraction_of_side_bearing}.
    # e.g. {"vo": -0.5} shifts "o" left by 0.5 * side_bearing units after "v".
    # Plain class attribute (not a dataclass field) so the YAML overlay and the
    # __init__ defaults rebuild in apply_config_overrides leave it untouched.
    kerning = {
        "ka": -0.55,
        "ke": -0.75,
        "kc": -0.75,
        "ko": -0.75,
        "ks": -0.55,
        # f letter
        "ff": -0.8,
        "ft": -0.55,
        "fa": -0.5,
        "fe": -0.5,
        "fc": -0.5,
        "fo": -0.5,
        "fs": -0.5,
        "af": -0.5,
        "of": -0.5,
        "ef": -0.5,
        "cf": -0.5,
        "sf": -0.5,
        "hf": -0.5,
        # t letter kerning
        "tt": -0.28,
        "ta": -0.1,
        "te": -0.1,
        "tc": -0.1,
        "to": -0.1,
        "ts": -0.1,
        "at": -0.4,
        "ot": -0.4,
        "et": -0.4,
        "ct": -0.4,
        "st": -0.4,
        "ht": -0.4,
        # r letter kerning
        "ra": -0.6,
        "re": -0.6,
        "rc": -0.6,
        "ro": -0.6,
        "rs": -0.6,
        "rd": -0.6,
        "rq": -0.6,
        # v letter kerning
        "va": -0.4,
        "ve": -0.2,
        "vc": -0.2,
        "vo": -0.2,
        "vs": -0.2,
        "av": -0.2,
        "ov": -0.2,
        "ev": -0.25,
        "cv": -0.2,
        "sv": -0.2,
        "hv": -0.2,
        # y lette5 spacing
        "ya": -0.4,
        "ye": -0.2,
        "yc": -0.2,
        "yo": -0.2,
        "ys": -0.2,
        "ay": -0.3,
        "oy": -0.3,
        "ey": -0.2,
        "cy": -0.2,
        "sy": -0.2,
        "hy": -0.2,
        "by": -0.2,
        "py": -0.2,
        # w letter kerning
        "wa": -0.3,
        "we": -0.1,
        "wc": -0.1,
        "wo": -0.1,
        "ws": -0.1,
        "aw": -0.2,
        "ow": -0.2,
        "ew": -0.2,
        "cw": -0.2,
        "sw": -0.2,
        "hw": -0.1,
        "bw": -0.1,
        "pw": -0.1,
        # x letter kerning
        "xo": -0.2,
        "xa": -0.1,
        "xe": -0.2,
        "xc": -0.2,
        "ox": -0.2,
        "ex": -0.2,
        "cx": -0.2,
        # A letter kerning
        "AV": -2,
        # T letter kerning
        "Th": -0.8,
        "Ta": -1.6,
        "To": -1.6,
        "Te": -1.6,
        "Tr": -1.6,
        "TA": -1.5,
        "AT": -1.2,
        "OT": -0.4,
        # number kerning
        "67": -0.8,
        "69": -0.6,
    }


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
    stroke_x: int = FontConfig.stroke_x
    stroke_y: int = FontConfig.stroke_y
    stroke_alt: int = FontConfig.stroke_alt
    v_overshoot: int = FontConfig.v_overshoot
    h_overshoot: int = FontConfig.h_overshoot

    italic: bool = False

    @classmethod
    def weight(cls, w=400):
        """Return a DrawConfig with heavier stroke weights for a bold variant."""
        from math import log, exp

        brx = 1.7
        ratio_x = exp((w - 400) * log(brx) / 300)

        bry = 1.2
        ratio_y = exp((w - 400) * log(bry) / 300)

        bhy = 1.3
        hy_ratio = exp((w - 400) * log(bhy) / 300)

        # Function mapping 100 → 0.5 and 700 → 0.2
        taper = min(0.5, 0.5 - 0.0009 * (w - 400))

        extra_height = int((ratio_y - 1) * cls.stroke_y)
        return cls(
            stroke_x=int(cls.stroke_x * ratio_x),
            stroke_y=int(cls.stroke_y * ratio_y),
            stroke_alt=int(cls.stroke_alt * ratio_y),
            x_height=cls.x_height + extra_height,
            cap=cls.cap + extra_height,
            accent=cls.cap + extra_height,
            accent_cap=cls.accent_cap + extra_height,
            ascent=cls.ascent + extra_height,
            descent=cls.descent - extra_height,
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
