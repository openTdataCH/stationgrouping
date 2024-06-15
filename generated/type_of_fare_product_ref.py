from dataclasses import dataclass

from generated.type_of_fare_product_ref_structure import (
    TypeOfFareProductRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfFareProductRef(TypeOfFareProductRefStructure):
    """
    Reference to a TYPE OF FARE PRODUCT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
