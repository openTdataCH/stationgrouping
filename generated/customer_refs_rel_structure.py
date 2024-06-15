from dataclasses import dataclass, field
from typing import List

from generated.customer_ref import CustomerRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to CUSTOMER.
    """

    class Meta:
        name = "customerRefs_RelStructure"

    customer_ref: List[CustomerRef] = field(
        default_factory=list,
        metadata={
            "name": "CustomerRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
