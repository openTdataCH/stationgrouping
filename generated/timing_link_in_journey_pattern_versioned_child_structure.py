from dataclasses import dataclass, field
from typing import Optional

from generated.journey_run_times_rel_structure import (
    JourneyRunTimesRelStructure,
)
from generated.link_in_link_sequence_versioned_child_structure import (
    LinkInLinkSequenceVersionedChildStructure,
)
from generated.timing_link_ref import TimingLinkRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingLinkInJourneyPatternVersionedChildStructure(
    LinkInLinkSequenceVersionedChildStructure
):
    """
    Type for TIMING LINK IN JOURNEY PATTERN.

    :ivar timing_link_ref:
    :ivar run_times: run times for this TIMING LINK.
    """

    class Meta:
        name = "TimingLinkInJourneyPattern_VersionedChildStructure"

    timing_link_ref: TimingLinkRef = field(
        metadata={
            "name": "TimingLinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    run_times: Optional[JourneyRunTimesRelStructure] = field(
        default=None,
        metadata={
            "name": "runTimes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
