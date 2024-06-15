from dataclasses import dataclass, field
from typing import Optional

from generated.fare_product_version_structure import (
    FareProductVersionStructure,
)
from generated.preassigned_fare_product_enumeration import (
    PreassignedFareProductEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PreassignedFareProductVersionStructure(FareProductVersionStructure):
    """
    Type for PREASSIGNED FARE PRODUCT.

    :ivar product_type: Classification of PEEASSIGNED FARE PRODUCT.
        +v1.1
    """

    class Meta:
        name = "PreassignedFareProduct_VersionStructure"

    product_type: Optional[PreassignedFareProductEnumeration] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
