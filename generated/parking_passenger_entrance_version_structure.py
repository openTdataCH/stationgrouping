from dataclasses import dataclass, field
from typing import Optional

from generated.parking_area_refs_rel_structure import (
    ParkingAreaRefsRelStructure,
)
from generated.site_entrance_version_structure import (
    SiteEntranceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPassengerEntranceVersionStructure(SiteEntranceVersionStructure):
    """
    Type for a PARKING PASSENGER ENTRANCe.

    :ivar areas: PARKING AREA to which prperties appky +v1.1.
    """

    class Meta:
        name = "ParkingPassengerEntrance_VersionStructure"

    areas: Optional[ParkingAreaRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
