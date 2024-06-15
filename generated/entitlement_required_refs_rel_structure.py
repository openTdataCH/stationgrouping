from dataclasses import dataclass, field
from typing import List

from generated.entitlement_required_ref import EntitlementRequiredRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntitlementRequiredRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for references to a ENTITLEMENT REQUIRED PARAMETER.
    """

    class Meta:
        name = "entitlementRequiredRefs_RelStructure"

    entitlement_required_ref: List[EntitlementRequiredRef] = field(
        default_factory=list,
        metadata={
            "name": "EntitlementRequiredRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
