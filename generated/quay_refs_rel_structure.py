from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.quay_ref import QuayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QuayRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a QUAY.
    """

    class Meta:
        name = "quayRefs_RelStructure"

    quay_ref: List[QuayRef] = field(
        default_factory=list,
        metadata={
            "name": "QuayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
