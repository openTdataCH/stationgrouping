from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class CheckServiceEnumeration(Enum):
    """
    Allowed values for a CHECK CONSTRAINT service.
    """

    SELF_SERVICE = "selfService"
    COUNTER_SERVICE = "counterService"
    ANY_SERVICE = "anyService"
    OTHER = "other"
