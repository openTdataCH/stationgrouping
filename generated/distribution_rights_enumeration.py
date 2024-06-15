from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class DistributionRightsEnumeration(Enum):
    """
    Allowed values for DISTRIBUTION RIGHTs.
    """

    NONE = "none"
    SELL = "sell"
    EXCHANGE = "exchange"
    REFUND = "refund"
    INFORM = "inform"
    PRIVATE = "private"
    OTHER = "other"
