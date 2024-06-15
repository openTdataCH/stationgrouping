from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ParkingLayoutEnumeration(Enum):
    """
    Allowed values for PARKING Layout types.
    """

    COVERED = "covered"
    OPEN_SPACE = "openSpace"
    MULTISTOREY = "multistorey"
    UNDERGROUND = "underground"
    ROADSIDE = "roadside"
    UNDEFINED = "undefined"
    OTHER = "other"
    CYCLE_HIRE = "cycleHire"
