from dataclasses import dataclass

from generated.dated_vehicle_journey_version_structure import (
    DatedVehicleJourneyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DatedVehicleJourney(DatedVehicleJourneyVersionStructure):
    """
    A particular journey of a vehicle on a particular OPERATING DAY including all
    modifications possibly decided by the control staff.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
