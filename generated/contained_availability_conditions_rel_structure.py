from dataclasses import dataclass, field
from typing import List

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.entity_in_version_structure import AvailabilityCondition

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ContainedAvailabilityConditionsRelStructure(
    ContainmentAggregationStructure
):
    """
    A collection of one or more AVAILABILITY CONDITIONs.
    """

    class Meta:
        name = "containedAvailabilityConditions_RelStructure"

    availability_condition: List[AvailabilityCondition] = field(
        default_factory=list,
        metadata={
            "name": "AvailabilityCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
