from dataclasses import dataclass, field
from typing import Optional

from generated.destination_display_views_rel_structure import (
    DestinationDisplayViewsRelStructure,
)
from generated.flexible_quay_version_structure import (
    FlexibleQuayVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleAreaVersionStructure(FlexibleQuayVersionStructure):
    """
    Type for a FLEXIBLE AREA.

    :ivar destinations: Destination headings for FLEXIBLE AREa.
    """

    class Meta:
        name = "FlexibleArea_VersionStructure"

    destinations: Optional[DestinationDisplayViewsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
