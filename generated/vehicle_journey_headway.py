from dataclasses import dataclass

from generated.vehicle_journey_headway_versioned_child_structure import (
    VehicleJourneyHeadwayVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyHeadway(VehicleJourneyHeadwayVersionedChildStructure):
    """Headway interval information that is available for a VEHICLE JOURNEY (to be
    understood as the delay between the previous and the next VEHICLE JOURNEY).

    This information must be consistent with HEADWAY JOURNEY GROUP if
    available (HEADWAY JOURNEY GROUP being a more detailed way of
    describing headway services).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
