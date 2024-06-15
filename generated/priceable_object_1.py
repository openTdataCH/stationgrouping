from dataclasses import dataclass

from generated.priceable_object_version_structure import (
    PriceableObjectVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceableObject1(PriceableObjectVersionStructure):
    """
    An element that may have a FARE PRICE.
    """

    class Meta:
        name = "PriceableObject"
        namespace = "http://www.netex.org.uk/netex"
