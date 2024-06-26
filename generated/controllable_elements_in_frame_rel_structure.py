from dataclasses import dataclass, field
from typing import List

from generated.controllable_element import ControllableElement
from generated.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControllableElementsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of CONTROLLABLE ELEMENTs.
    """

    class Meta:
        name = "controllableElementsInFrame_RelStructure"

    controllable_element: List[ControllableElement] = field(
        default_factory=list,
        metadata={
            "name": "ControllableElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
