from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.point_of_interest_space import PointOfInterestSpace
from generated.site_component_ref_structure import SiteComponentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestSpacesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of POINT OF INTEREST SPACEs.
    """

    class Meta:
        name = "pointOfInterestSpaces_RelStructure"

    point_of_interest_space_ref_or_point_of_interest_space: List[
        Union[SiteComponentRefStructure, PointOfInterestSpace]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PointOfInterestSpaceRef",
                    "type": SiteComponentRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestSpace",
                    "type": PointOfInterestSpace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
