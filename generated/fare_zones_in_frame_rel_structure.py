from dataclasses import dataclass, field
from typing import List

from generated.fare_zone import FareZone
from generated.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareZonesInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of FARE ZONE.
    """

    class Meta:
        name = "fareZonesInFrame_RelStructure"

    fare_zone: List[FareZone] = field(
        default_factory=list,
        metadata={
            "name": "FareZone",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
