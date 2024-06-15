from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.headway_journey_group import HeadwayJourneyGroup
from generated.headway_journey_group_ref import HeadwayJourneyGroupRef
from generated.rhythmical_journey_group import RhythmicalJourneyGroup
from generated.rhythmical_journey_group_ref import RhythmicalJourneyGroupRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FrequencyGroupsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of a VEHICLE JOURNEY FREQUENCies.
    """

    class Meta:
        name = "frequencyGroups_RelStructure"

    choice: List[
        Union[
            HeadwayJourneyGroupRef,
            HeadwayJourneyGroup,
            RhythmicalJourneyGroupRef,
            RhythmicalJourneyGroup,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "HeadwayJourneyGroupRef",
                    "type": HeadwayJourneyGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadwayJourneyGroup",
                    "type": HeadwayJourneyGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RhythmicalJourneyGroupRef",
                    "type": RhythmicalJourneyGroupRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RhythmicalJourneyGroup",
                    "type": RhythmicalJourneyGroup,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
