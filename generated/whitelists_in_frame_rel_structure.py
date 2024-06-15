from dataclasses import dataclass, field
from typing import List

from generated.frame_containment_structure import FrameContainmentStructure
from generated.whitelist import Whitelist

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WhitelistsInFrameRelStructure(FrameContainmentStructure):
    """Type for containment in frame of BLACK LISTS.

    +v1.1
    """

    class Meta:
        name = "whitelistsInFrame_RelStructure"

    whitelist: List[Whitelist] = field(
        default_factory=list,
        metadata={
            "name": "Whitelist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
