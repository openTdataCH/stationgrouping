from dataclasses import dataclass, field
from typing import Optional, Union

from generated.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from generated.journey_pattern_ref import JourneyPatternRef
from generated.journey_wait_time_versioned_child_structure import (
    JourneyWaitTimeVersionedChildStructure,
)
from generated.service_journey_pattern_ref import ServiceJourneyPatternRef
from generated.service_pattern_ref import ServicePatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternWaitTimeVersionedChildStructure(
    JourneyWaitTimeVersionedChildStructure
):
    """
    Type for JOURNEY PATTERN WAIT TIME.
    """

    class Meta:
        name = "JourneyPatternWaitTime_VersionedChildStructure"

    choice_1: Optional[
        Union[
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
