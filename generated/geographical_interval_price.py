from dataclasses import dataclass

from generated.geographical_interval_price_versioned_child_structure import (
    GeographicalIntervalPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalIntervalPrice(
    GeographicalIntervalPriceVersionedChildStructure
):
    """A set of all possible price features of a GEOGRAPHICAL INTERVAL: default total price etc."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
