from dataclasses import dataclass

from generated.geographical_unit_prices_rel_structure import (
    GeographicalUnitPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalUnitPrice(GeographicalUnitPriceVersionedChildStructure):
    """A set of all possible price features of a GEOGRAPHICAL UNIT: default total price etc."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
