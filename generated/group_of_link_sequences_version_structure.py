from dataclasses import dataclass, field
from typing import Optional

from generated.group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from generated.link_sequence_refs_rel_structure import (
    LinkSequenceRefsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinkSequencesVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for GROUP OF LINK SEQUENCEs.

    :ivar members: LINK SEQUENCEs in GROUP OF LINK SEQUENCEs.
    """

    class Meta:
        name = "GroupOfLinkSequences_VersionStructure"

    members: Optional[LinkSequenceRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
