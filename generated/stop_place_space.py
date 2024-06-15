from dataclasses import dataclass

from generated.stop_place_space_version_structure import (
    StopPlaceSpaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceSpace(StopPlaceSpaceVersionStructure):
    """
    A physical area within a STOP PLACE, for example, a QUAY, BOARDING POSITION,
    ACCESS SPACE or EQUIPMENT PLACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
