from dataclasses import dataclass

from generated.geographical_unit_price_ref_structure import (
    GeographicalUnitPriceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeographicalUnitPriceRef(GeographicalUnitPriceRefStructure):
    """
    Reference to a GEOGRAPHICAL UNIT PRICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
