from dataclasses import dataclass, field
from typing import List

from generated.frame_containment_structure import FrameContainmentStructure
from generated.retail_device import RetailDevice

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailDevicesInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of CUSTOMERs.
    """

    class Meta:
        name = "retailDevicesInFrame_RelStructure"

    retail_device: List[RetailDevice] = field(
        default_factory=list,
        metadata={
            "name": "RetailDevice",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
