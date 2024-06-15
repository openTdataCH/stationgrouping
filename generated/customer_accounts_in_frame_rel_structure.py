from dataclasses import dataclass, field
from typing import List

from generated.customer_account import CustomerAccount
from generated.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerAccountsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of CUSTOMER ACCOUNTs.
    """

    class Meta:
        name = "customerAccountsInFrame_RelStructure"

    customer_account: List[CustomerAccount] = field(
        default_factory=list,
        metadata={
            "name": "CustomerAccount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
