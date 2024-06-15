from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.offered_travel_specification import OfferedTravelSpecification
from generated.offered_travel_specification_ref import (
    OfferedTravelSpecificationRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OfferedTravelSpecificationsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TRAVEL SPECIFICATIONs.
    """

    class Meta:
        name = "offeredTravelSpecifications_RelStructure"

    offered_travel_specification_ref_or_offered_travel_specification: List[
        Union[OfferedTravelSpecificationRef, OfferedTravelSpecification]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OfferedTravelSpecificationRef",
                    "type": OfferedTravelSpecificationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OfferedTravelSpecification",
                    "type": OfferedTravelSpecification,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
