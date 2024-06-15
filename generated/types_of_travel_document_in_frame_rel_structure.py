from dataclasses import dataclass, field
from typing import List

from generated.frame_containment_structure import FrameContainmentStructure
from generated.type_of_travel_document import TypeOfTravelDocument

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypesOfTravelDocumentInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of TYPE OF TRAVEL DOCUMENT.
    """

    class Meta:
        name = "typesOfTravelDocumentInFrame_RelStructure"

    type_of_travel_document: List[TypeOfTravelDocument] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfTravelDocument",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
