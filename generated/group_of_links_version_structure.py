from dataclasses import dataclass, field
from typing import Optional

from generated.group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from generated.link_refs_rel_structure import LinkRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinksVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for GROUP OF LINKs.

    :ivar members: Links in group.
    """

    class Meta:
        name = "GroupOfLinks_VersionStructure"

    members: Optional[LinkRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
