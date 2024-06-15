from dataclasses import dataclass

from generated.time_interval_price_ref_structure import (
    TimeIntervalPriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeIntervalPriceRef(TimeIntervalPriceRefStructure):
    """
    Reference to a TIME INTERVAL PRICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
