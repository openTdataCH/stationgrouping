from dataclasses import dataclass, field
from typing import List

from generated.distance_matrix_element import DistanceMatrixElement
from generated.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfDistanceMatrixElementsInFrameRelStructure(
    FrameContainmentStructure
):
    """
    Type for containment in frame of GROUPS OF DISTANCE MATRIX ELEMENTs.
    """

    class Meta:
        name = "groupsOfDistanceMatrixElementsInFrame_RelStructure"

    distance_matrix_element: List[DistanceMatrixElement] = field(
        default_factory=list,
        metadata={
            "name": "DistanceMatrixElement",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
