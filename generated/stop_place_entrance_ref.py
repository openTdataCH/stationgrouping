from dataclasses import dataclass

from generated.stop_place_entrance_ref_structure import (
    StopPlaceEntranceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceEntranceRef(StopPlaceEntranceRefStructure):
    """
    Reference to a STOP PLACE ENTRANCE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
