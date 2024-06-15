from dataclasses import dataclass

from generated.boarding_position_version_structure import (
    BoardingPositionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BoardingPosition(BoardingPositionVersionStructure):
    """
    A location within a QUAY from which passengers may directly board, or onto
    which passengers may directly alight from, a VEHICLE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
