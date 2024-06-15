from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CycleStorageEnumeration(Enum):
    """
    Allowed value for Cycle Storage.
    """

    RACKS = "racks"
    BARS = "bars"
    RAILINGS = "railings"
    CYCLE_SCHEME = "cycleScheme"
    OTHER = "other"
