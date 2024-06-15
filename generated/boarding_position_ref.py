from dataclasses import dataclass

from generated.boarding_position_ref_structure import (
    BoardingPositionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BoardingPositionRef(BoardingPositionRefStructure):
    """
    Reference to a BOARDING POSITION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
