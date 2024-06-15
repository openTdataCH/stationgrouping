from dataclasses import dataclass, field
from typing import List

from generated.blacklist_ref import BlacklistRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BlacklistRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of BLACKLISTs.
    """

    class Meta:
        name = "blacklistRefs_RelStructure"

    blacklist_ref: List[BlacklistRef] = field(
        default_factory=list,
        metadata={
            "name": "BlacklistRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
