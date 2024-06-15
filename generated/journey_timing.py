from dataclasses import dataclass

from generated.journey_timing_versioned_child_structure import (
    JourneyTimingVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyTiming(JourneyTimingVersionedChildStructure):
    """
    A  time-related information referring to journey timing whose value depends on
    the time of use and so can be associated with a TIME DEMAND TYPE, TIME BAND or
    OPERATIONAL CONTEXT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
