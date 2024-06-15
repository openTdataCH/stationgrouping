from dataclasses import dataclass, field
from typing import List

from generated.frame_containment_structure import FrameContainmentStructure
from generated.sales_offer_package_substitution import (
    SalesOfferPackageSubstitution,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageSubstitutionsInFrameRelStructure(
    FrameContainmentStructure
):
    """
    Type for containment in frame of SALES OFFER PACKAGE SUBSTITUTIONs.
    """

    class Meta:
        name = "salesOfferPackageSubstitutionsInFrame_RelStructure"

    sales_offer_package_substitution: List[SalesOfferPackageSubstitution] = (
        field(
            default_factory=list,
            metadata={
                "name": "SalesOfferPackageSubstitution",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
                "min_occurs": 1,
            },
        )
    )
