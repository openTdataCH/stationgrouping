from dataclasses import dataclass, field
from typing import List

from generated.frame_containment_structure import FrameContainmentStructure
from generated.travel_document import TravelDocument

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelDocumentsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of TRAVEL DOCUMENT.
    """

    class Meta:
        name = "travelDocumentsInFrame_RelStructure"

    travel_document: List[TravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TravelDocument",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
