from dataclasses import dataclass, field
from typing import Any

from generated.stop_place_derived_view_structure import (
    StopPlaceDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopPlaceView(StopPlaceDerivedViewStructure):
    """Simplified view of STOP PLACE.

    Contains.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    branding_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
