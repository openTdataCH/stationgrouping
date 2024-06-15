from dataclasses import dataclass, field
from typing import List, Union

from generated.amount_of_price_unit_product import AmountOfPriceUnitProduct
from generated.capped_discount_right import CappedDiscountRight
from generated.frame_containment_structure import FrameContainmentStructure
from generated.preassigned_fare_product import PreassignedFareProduct
from generated.sale_discount_right import SaleDiscountRight
from generated.supplement_product import SupplementProduct
from generated.third_party_product import ThirdPartyProduct
from generated.usage_discount_right import UsageDiscountRight

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareProductsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of FARE PRODUCT.
    """

    class Meta:
        name = "fareProductsInFrame_RelStructure"

    choice: List[
        Union[
            SupplementProduct,
            PreassignedFareProduct,
            AmountOfPriceUnitProduct,
            CappedDiscountRight,
            UsageDiscountRight,
            ThirdPartyProduct,
            SaleDiscountRight,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplementProduct",
                    "type": SupplementProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProduct",
                    "type": PreassignedFareProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProduct",
                    "type": AmountOfPriceUnitProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRight",
                    "type": CappedDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRight",
                    "type": UsageDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProduct",
                    "type": ThirdPartyProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRight",
                    "type": SaleDiscountRight,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
