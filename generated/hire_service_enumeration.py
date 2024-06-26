from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class HireServiceEnumeration(Enum):
    """
    Allowed values for HIRE SERVICE.
    """

    CYCLE_HIRE = "cycleHire"
    MOTORCYCLE_HIRE = "motorcycleHire"
    CAR_HIRE = "carHire"
    RECREATIONAL_DEVICE_HIRE = "recreationalDeviceHire"
