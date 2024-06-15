from dataclasses import dataclass, field
from typing import Optional

from generated.boarding_position_type_enumeration import (
    BoardingPositionTypeEnumeration,
)
from generated.entrance_refs_rel_structure import EntranceRefsRelStructure
from generated.stop_place_space_version_structure import (
    StopPlaceSpaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BoardingPositionVersionStructure(StopPlaceSpaceVersionStructure):
    """
    Type for a BOARDING POSITION.

    :ivar public_code: Pubic identifier code of BOARDING POSITION.
    :ivar boarding_position_type: Classifier of BOARDING POSITION.
    :ivar boarding_position_entrances: Entrances to BOARDING POSITION.
    """

    class Meta:
        name = "BoardingPosition_VersionStructure"

    public_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_position_type: Optional[BoardingPositionTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "BoardingPositionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_position_entrances: Optional[EntranceRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "boardingPositionEntrances",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
