from dataclasses import dataclass, field
from typing import List

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.operational_context_ref import OperationalContextRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperationalContexRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to an OPERATIONAL CONTEXT.
    """

    class Meta:
        name = "operationalContexRefs_RelStructure"

    operational_context_ref: List[OperationalContextRef] = field(
        default_factory=list,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        },
    )
