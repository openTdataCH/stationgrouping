from dataclasses import dataclass, field
from typing import List

from generated.entitlement_given_ref import EntitlementGivenRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementGivenRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for references to a ENTITLEMENT GIVEN PARAMETER.
    """

    class Meta:
        name = "entitlementGivenRefs_RelStructure"

    entitlement_given_ref: List[EntitlementGivenRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementGivenRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
