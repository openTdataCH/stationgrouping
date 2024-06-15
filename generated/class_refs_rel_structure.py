from dataclasses import dataclass, field
from typing import List, Union

from generated.class_in_frame_ref import ClassInFrameRef
from generated.class_ref import ClassRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClassRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of Classes.
    """

    class Meta:
        name = "classRefs_RelStructure"

    class_in_frame_ref_or_class_ref: List[Union[ClassInFrameRef, ClassRef]] = (
        field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "ClassInFrameRef",
                        "type": ClassInFrameRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ClassRef",
                        "type": ClassRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
