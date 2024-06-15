from dataclasses import dataclass, field
from typing import List, Union

from generated.authority_ref import AuthorityRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.operator_ref import OperatorRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportOrganisationRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to an OPERATOR.
    """

    class Meta:
        name = "transportOrganisationRefs_RelStructure"

    authority_ref_or_operator_ref: List[Union[AuthorityRef, OperatorRef]] = (
        field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "AuthorityRef",
                        "type": AuthorityRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "OperatorRef",
                        "type": OperatorRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
