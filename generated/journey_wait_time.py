from dataclasses import dataclass

from generated.journey_wait_time_versioned_child_structure import (
    JourneyWaitTimeVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyWaitTime(JourneyWaitTimeVersionedChildStructure):
    """The time a vehicle has to wait at a specific TIMING POINT IN JOURNEY
    PATTERN, for a specified TIME DEMAND TYPE.

    This wait time can be superseded by a VEHICLE JOURNEY WAIT TIME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
