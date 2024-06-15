from dataclasses import dataclass

from generated.normal_dated_vehicle_journey_version_structure import (
    NormalDatedVehicleJourneyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NormalDatedVehicleJourney(NormalDatedVehicleJourneyVersionStructure):
    """
    A DATED VEHICLE JOURNEY identical to a long-term planned VEHICLE JOURNEY,
    possibly updated according to short-term modifications of the PRODUCTION PLAN
    decided by the control staff.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
