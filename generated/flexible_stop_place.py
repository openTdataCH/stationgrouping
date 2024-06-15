from dataclasses import dataclass

from generated.flexible_stop_place_version_structure import (
    FlexibleStopPlaceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleStopPlace(FlexibleStopPlaceVersionStructure):
    """
    A named type of STOP PLACE for DRT comprising one or more flexible zones where
    vehicles may stop and where passengers may board or leave vehicles.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
