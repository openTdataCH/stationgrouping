from dataclasses import dataclass

from generated.time_unit_price_versioned_child_structure import (
    TimeUnitPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeUnitPrice(TimeUnitPriceVersionedChildStructure):
    """A set of all possible price features of a TIME UNIT: default total price etc."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
