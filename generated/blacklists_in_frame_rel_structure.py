from dataclasses import dataclass, field
from typing import List

from generated.blacklist import Blacklist
from generated.frame_containment_structure import FrameContainmentStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BlacklistsInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of BLACK LISTS.
    """

    class Meta:
        name = "blacklistsInFrame_RelStructure"

    blacklist: List[Blacklist] = field(
        default_factory=list,
        metadata={
            "name": "Blacklist",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
