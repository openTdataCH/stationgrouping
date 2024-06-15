from dataclasses import dataclass

from generated.vehicle_journey_version_structure import (
    VehicleJourneyVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourney(VehicleJourneyVersionStructure):
    """
    The planned movement of a public transport vehicle on a DAY TYPE from the start
    point to the end point of a JOURNEY PATTERN on a specified ROUTE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
