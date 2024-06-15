from dataclasses import dataclass, field
from typing import List

from generated.border_point import BorderPoint
from generated.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BorderPointsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of BORDER POINT.
    """

    class Meta:
        name = "borderPointsInFrame_RelStructure"

    border_point: List[BorderPoint] = field(
        default_factory=list,
        metadata={
            "name": "BorderPoint",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
