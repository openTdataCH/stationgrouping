from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ZoneUseEnumeration(Enum):
    """
    Allowed values for Zone Use.
    """

    CANNOT_BOARD_AND_ALIGHT_IN_SAME_ZONE = "cannotBoardAndAlightInSameZone"
    MUST_ALIGHT_IN_ZONE = "mustAlightInZone"
    CANNOT_ALIGHT_IN_ZONE = "cannotAlightInZone"
    OTHER = "other"
