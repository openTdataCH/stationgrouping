from dataclasses import dataclass, field
from typing import List

from generated.frame_containment_structure import FrameContainmentStructure
from generated.sales_offer_package_element import SalesOfferPackageElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageElementsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of SALES OFFER PACKAGE Element.
    """

    class Meta:
        name = "salesOfferPackageElementsInFrame_RelStructure"

    sales_offer_package_element: List[SalesOfferPackageElement] = field(
        default_factory=list,
        metadata={
            "name": "SalesOfferPackageElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
