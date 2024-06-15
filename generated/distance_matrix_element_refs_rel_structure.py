from dataclasses import dataclass, field
from typing import List, Union

from generated.distance_matrix_element_inverse_ref import (
    DistanceMatrixElementInverseRef,
)
from generated.distance_matrix_element_ref import DistanceMatrixElementRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistanceMatrixElementRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of DISTANCE MATRIX ELEMENTs.
    """

    class Meta:
        name = "distanceMatrixElementRefs_RelStructure"

    distance_matrix_element_ref_or_distance_matrix_element_inverse_ref: List[
        Union[DistanceMatrixElementRef, DistanceMatrixElementInverseRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistanceMatrixElementRef",
                    "type": DistanceMatrixElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementInverseRef",
                    "type": DistanceMatrixElementInverseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
