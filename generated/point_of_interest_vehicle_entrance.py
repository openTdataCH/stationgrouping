from dataclasses import dataclass, field
from typing import Any

from generated.point_of_interest_vehicle_entrance_version_structure import (
    PointOfInterestVehicleEntranceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestVehicleEntrance(
    PointOfInterestVehicleEntranceVersionStructure
):
    """
    A VEHICLE ENTRANCE to a POINT OF INTEREST.

    :ivar members: POINTs in GROUP OF POINTs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    members: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
