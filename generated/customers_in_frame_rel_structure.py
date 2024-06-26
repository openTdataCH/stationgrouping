from dataclasses import dataclass, field
from typing import List

from generated.customer import Customer
from generated.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomersInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of CUSTOMERs.
    """

    class Meta:
        name = "customersInFrame_RelStructure"

    customer: List[Customer] = field(
        default_factory=list,
        metadata={
            "name": "Customer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
