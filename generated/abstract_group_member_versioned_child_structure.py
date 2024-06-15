from dataclasses import dataclass, field
from typing import Optional

from generated.entity_in_version_structure import VersionedChildStructure
from generated.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AbstractGroupMemberVersionedChildStructure(VersionedChildStructure):
    """Type for a GROUP OF ENTITY MEMBERs.

    Subclass this for specific member types.

    :ivar description:
    :ivar order: Order of member within parent group.
    """

    class Meta:
        name = "AbstractGroupMember_VersionedChildStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
