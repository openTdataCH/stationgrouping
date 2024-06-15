from dataclasses import dataclass, field
from typing import List, Union

from generated.access_space import AccessSpace
from generated.access_space_ref import AccessSpaceRef
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessSpacesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of ACCESS SPACEs.
    """

    class Meta:
        name = "accessSpaces_RelStructure"

    access_space_ref_or_access_space: List[
        Union[AccessSpaceRef, AccessSpace]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccessSpaceRef",
                    "type": AccessSpaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessSpace",
                    "type": AccessSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
