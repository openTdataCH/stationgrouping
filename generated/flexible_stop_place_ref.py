from dataclasses import dataclass

from generated.flexible_stop_place_ref_structure import (
    FlexibleStopPlaceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleStopPlaceRef(FlexibleStopPlaceRefStructure):
    """
    Reference to a FLEXIBLE STOP PLACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
