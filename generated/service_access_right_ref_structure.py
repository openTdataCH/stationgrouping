from dataclasses import dataclass

from generated.priceable_object_ref_structure import (
    PriceableObjectRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceAccessRightRefStructure(PriceableObjectRefStructure):
    """
    Type for Reference to a SERVICE ACCESS RIGHT.
    """