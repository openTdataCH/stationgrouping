from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class RoutingTypeEnumeration(Enum):
    """
    Allowed values for Routing Type.
    """

    DIRECT = "direct"
    INDIRECT = "indirect"
    BOTH = "both"
