from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class ActivationMeansEnumeration(Enum):
    """
    Allowed values for Activation Means.
    """

    NONE_REQUIRED = "noneRequired"
    CHECK_IN = "checkIn"
    USE_OF_VALIDATOR = "useOfValidator"
    USE_OF_MOBILE_DEVICE = "useOfMobileDevice"
    AUTOMATIC_BY_TIME = "automaticByTime"
    AUTOMATIC_BY_PROXIMITY = "automaticByProximity"
    OTHER = "other"
