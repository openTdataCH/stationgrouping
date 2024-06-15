from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.time_unit import TimeUnit
from generated.time_unit_ref import TimeUnitRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeUnitsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TIME UNITs.
    """

    class Meta:
        name = "timeUnits_RelStructure"

    time_unit_ref_or_time_unit: List[Union[TimeUnitRef, TimeUnit]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeUnitRef",
                    "type": TimeUnitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnit",
                    "type": TimeUnit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )