from dataclasses import dataclass, field
from typing import Optional

from generated.group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from generated.timeband_refs_rel_structure import TimebandRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfTimebandsVersionedChildStructure(GroupOfEntitiesVersionStructure):
    """
    Type for a GROUP OF TIMEBANDS.

    :ivar timebands: The (inclusive) start time.
    """

    class Meta:
        name = "GroupOfTimebands_VersionedChildStructure"

    timebands: Optional[TimebandRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
