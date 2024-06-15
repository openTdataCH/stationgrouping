from dataclasses import dataclass, field
from typing import List

from generated.group_of_operators_ref import GroupOfOperatorsRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupsOfTransportOrganisationsRefsRelStructure(
    OneToManyRelationshipStructure
):
    """
    Type for a list of references to list of GROUPs OF TRANSPORT ORGANISATIONS.
    """

    class Meta:
        name = "groupsOfTransportOrganisationsRefs_RelStructure"

    group_of_operators_ref: List[GroupOfOperatorsRef] = field(
        default_factory=list,
        metadata={
            "name": "GroupOfOperatorsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
