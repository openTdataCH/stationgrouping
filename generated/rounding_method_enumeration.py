from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RoundingMethodEnumeration(Enum):
    """
    Allowed values for ROUNDING METHOD.
    """

    NONE = "none"
    DOWN = "down"
    UP = "up"
    SPLIT = "split"
    STEP_TABLE = "stepTable"
