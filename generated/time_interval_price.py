from dataclasses import dataclass

from generated.time_interval_price_versioned_child_structure import (
    TimeIntervalPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeIntervalPrice(TimeIntervalPriceVersionedChildStructure):
    """A set of all possible price features of a TIME INTERVAL: default total price etc."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
