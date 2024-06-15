from dataclasses import dataclass, field
from typing import Any

from generated.stop_place_vehicle_entrance_version_structure import (
    StopPlaceVehicleEntranceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceVehicleEntrance(StopPlaceVehicleEntranceVersionStructure):
    """A physical entrance or exit to/from a SITE for a VEHICLE.

    May be a door, barrier, gate or other recognizable point of access.

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
