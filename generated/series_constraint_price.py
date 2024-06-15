from dataclasses import dataclass

from generated.series_constraint_price_versioned_child_structure import (
    SeriesConstraintPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SeriesConstraintPrice(SeriesConstraintPriceVersionedChildStructure):
    """A set of all possible price features of a SERIES CONSTRAINT: default total price, discount in value or percentage etc."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
