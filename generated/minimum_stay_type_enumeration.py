from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MinimumStayTypeEnumeration(Enum):
    """
    Allowed values for MINIMUM STAY Type.
    """

    NONE = "none"
    SPECIFIED_NIGHTS_AWAY = "specifiedNightsAway"
    COUNT_NIGHTS_AWAY = "countNightsAway"
    BOTH = "both"
    EITHER = "either"
