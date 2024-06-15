from dataclasses import dataclass, field
from typing import Optional, Union

from generated.dated_special_service_ref import DatedSpecialServiceRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.special_service_ref import SpecialServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpecialServiceRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list references to a SPECIAL SERVICE.
    """

    class Meta:
        name = "specialServiceRefs_RelStructure"

    dated_special_service_ref_or_special_service_ref: Optional[
        Union[DatedSpecialServiceRef, SpecialServiceRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DatedSpecialServiceRef",
                    "type": DatedSpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialServiceRef",
                    "type": SpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
