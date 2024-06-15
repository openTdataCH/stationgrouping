from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class SelfDriveSubmodeEnumeration(Enum):
    """Values for SelfDrive MODEs of TRANSPORT: TPEG pti_table_12."""

    UNKNOWN = "unknown"
    UNDEFINED = "undefined"
    HIRE_CAR = "hireCar"
    HIRE_VAN = "hireVan"
    HIRE_MOTORBIKE = "hireMotorbike"
    HIRE_CYCLE = "hireCycle"
    ALL_HIRE_VEHICLES = "allHireVehicles"
