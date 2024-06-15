from dataclasses import dataclass, field
from typing import Any

from generated.vehicle_stopping_position_version_structure import (
    VehicleStoppingPositionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleStoppingPosition(VehicleStoppingPositionVersionStructure):
    """
    Designated Position within a VEHICLE STOPPING PLACE for a Vehicle to stop.

    :ivar url: Default URL for ADDRESSABLE PLACE.
    :ivar image: Default image for ADDRESSABLE PLACE.
    :ivar postal_address:
    :ivar road_address: ADDRESS of a numbered building on a named road.
    :ivar members: POINTs in GROUP OF POINTs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    url: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    image: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    postal_address: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    road_address: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    members: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
