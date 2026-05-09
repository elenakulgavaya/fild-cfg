import warnings

warnings.warn(
    "fild-cfg is deprecated and will no longer be maintained. "
    "Migrate to surety-config: pip install surety-config. "
    "Replace 'from fild_cfg import Cfg' with 'from surety.config import Cfg'. "
    "See https://github.com/elenakulgavaya/surety-config for details.",
    DeprecationWarning,
    stacklevel=2,
)

from .config import Cfg
