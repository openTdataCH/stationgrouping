from dataclasses import dataclass

from generated.point_of_interest_vehicle_entrance_ref_structure import (
    PointOfInterestVehicleEntranceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestVehicleEntranceRef(
    PointOfInterestVehicleEntranceRefStructure
):
    """
    Reference to a POINT OF INTEREST VEHICLEENTRANCE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
