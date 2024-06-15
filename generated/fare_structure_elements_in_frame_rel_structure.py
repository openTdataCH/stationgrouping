from dataclasses import dataclass, field
from typing import List

from generated.fare_structure_element import FareStructureElement
from generated.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureElementsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of FARE STUCTURE ELEMENTs.
    """

    class Meta:
        name = "fareStructureElementsInFrame_RelStructure"

    fare_structure_element: List[FareStructureElement] = field(
        default_factory=list,
        metadata={
            "name": "FareStructureElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
