from dataclasses import dataclass, field
from typing import Any

from generated.stop_place_entrance_version_structure import (
    StopPlaceEntranceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceEntrance(StopPlaceEntranceVersionStructure):
    """
    Passenger Entrance to a STOP PLACE.

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
