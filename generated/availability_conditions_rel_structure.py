from dataclasses import dataclass, field
from typing import List, Union

from generated.availability_condition_ref import AvailabilityConditionRef
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.entity_in_version_structure import (
    AvailabilityCondition,
    ValidBetween,
    ValidDuring,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AvailabilityConditionsRelStructure(ContainmentAggregationStructure):
    """
    A collection of one or more AVAILABILITY CONDITIONs.
    """

    class Meta:
        name = "availabilityConditions_RelStructure"

    choice: List[
        Union[
            AvailabilityConditionRef,
            AvailabilityCondition,
            ValidDuring,
            ValidBetween,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AvailabilityConditionRef",
                    "type": AvailabilityConditionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AvailabilityCondition",
                    "type": AvailabilityCondition,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidDuring",
                    "type": ValidDuring,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidBetween",
                    "type": ValidBetween,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
