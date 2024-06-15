from dataclasses import dataclass, field
from typing import List

from generated.frame_containment_structure import FrameContainmentStructure
from generated.group_of_sales_offer_packages import GroupOfSalesOfferPackages

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfSalesOfferPackagesInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of GROUPs OF SALES OFFER PACKAGEs.
    """

    class Meta:
        name = "groupsOfSalesOfferPackagesInFrame_RelStructure"

    group_of_sales_offer_packages: List[GroupOfSalesOfferPackages] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfSalesOfferPackages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
