from dataclasses import dataclass

from generated.distance_matrix_element_price_versioned_child_structure import (
    DistanceMatrixElementPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementPrice(
    DistanceMatrixElementPriceVersionedChildStructure
):
    """A set of all possible price features of a DISTANCE MATRIX ELEMENT: default total price etc.
    ."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
