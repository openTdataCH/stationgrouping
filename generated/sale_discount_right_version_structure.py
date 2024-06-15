from dataclasses import dataclass, field
from typing import Optional, Union

from generated.fare_product_version_structure import (
    FareProductVersionStructure,
)
from generated.general_group_of_entities import GeneralGroupOfEntities
from generated.general_group_of_entities_ref import GeneralGroupOfEntitiesRef
from generated.sale_discount_right_enumeration import (
    SaleDiscountRightEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SaleDiscountRightVersionStructure(FareProductVersionStructure):
    """
    Type for SALES DISCOUNT RIGHT.

    :ivar product_type: Classification of USAGE DISOCUNT RIGHT. +v1.1
    :ivar general_group_of_entities_ref_or_general_group_of_entities:
    """

    class Meta:
        name = "SaleDiscountRight_VersionStructure"

    product_type: Optional[SaleDiscountRightEnumeration] = field(
        default=None,
        metadata={
            "name": "ProductType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    general_group_of_entities_ref_or_general_group_of_entities: Optional[
        Union[GeneralGroupOfEntitiesRef, GeneralGroupOfEntities]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeneralGroupOfEntitiesRef",
                    "type": GeneralGroupOfEntitiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralGroupOfEntities",
                    "type": GeneralGroupOfEntities,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
