from dataclasses import dataclass

from generated.distance_matrix_element_price_ref_structure import (
    DistanceMatrixElementPriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementPriceRef(DistanceMatrixElementPriceRefStructure):
    """
    Reference to a DISTANCE MATRIX ELEMENT PRICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
