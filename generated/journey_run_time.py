from dataclasses import dataclass

from generated.journey_run_time_versioned_child_structure import (
    JourneyRunTimeVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyRunTime(JourneyRunTimeVersionedChildStructure):
    """The time taken to traverse a TIMING LINK in a particular JOURNEY PATTERN,
    for a specified TIME DEMAND TYPE.

    If it exists, it will override the DEFAULT SERVICE JOURNEY RUN TIME
    and DEFAULT DEAD RUN RUN TIME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
