from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MedicalFacilityEnumeration(Enum):
    """
    Allowed values for Medical  Service Facility.
    """

    UNKNOWN = "unknown"
    DEFIBRILLATOR = "defibrillator"
    ALCOHOL_TEST = "alcoholTest"
