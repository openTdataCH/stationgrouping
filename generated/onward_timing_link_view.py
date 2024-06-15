from dataclasses import dataclass, field
from typing import Any

from generated.onward_timing_link_derived_view_structure import (
    OnwardTimingLinkDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnwardTimingLinkView(OnwardTimingLinkDerivedViewStructure):
    """
    Information about onwards TIMING LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    timing_link_in_journey_pattern_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    branding_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
