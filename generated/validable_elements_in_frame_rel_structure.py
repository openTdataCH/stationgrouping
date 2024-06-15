from dataclasses import dataclass, field
from typing import List

from generated.frame_containment_structure import FrameContainmentStructure
from generated.validable_element import ValidableElement

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidableElementsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of VALIDABLE ELEMENTs.
    """

    class Meta:
        name = "validableElementsInFrame_RelStructure"

    validable_element: List[ValidableElement] = field(
        default_factory=list,
        metadata={
            "name": "ValidableElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
