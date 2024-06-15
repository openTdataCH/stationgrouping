from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.retail_consortium_ref import RetailConsortiumRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailConsortiumRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of referecnes to RETAIL CONSORTIUMs.
    """

    class Meta:
        name = "retailConsortiumRefs_RelStructure"

    retail_consortium_ref: List[RetailConsortiumRef] = field(
        default_factory=list,
        metadata={
            "name": "RetailConsortiumRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
