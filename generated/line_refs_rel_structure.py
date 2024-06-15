from dataclasses import dataclass, field
from typing import List, Union

from generated.flexible_line_ref import FlexibleLineRef
from generated.line_ref import LineRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a LINE.
    """

    class Meta:
        name = "lineRefs_RelStructure"

    flexible_line_ref_or_line_ref: List[Union[FlexibleLineRef, LineRef]] = (
        field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "FlexibleLineRef",
                        "type": FlexibleLineRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "LineRef",
                        "type": LineRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
