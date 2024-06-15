from dataclasses import dataclass, field
from typing import List

from generated.strict_containment_aggregation_structure import (
    StrictContainmentAggregationStructure,
)
from generated.timetabled_passing_time import TimetabledPassingTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimetabledPassingTimesRelStructure(
    StrictContainmentAggregationStructure
):
    """
    Type for a list of TIMETABLED PASSING TIME.
    """

    class Meta:
        name = "timetabledPassingTimes_RelStructure"

    timetabled_passing_time: List[TimetabledPassingTime] = field(
        default_factory=list,
        metadata={
            "name": "TimetabledPassingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
