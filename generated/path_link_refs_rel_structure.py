from dataclasses import dataclass, field
from typing import List, Union

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.path_link_ref import PathLinkRef
from generated.path_link_ref_by_value import PathLinkRefByValue

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a PATH LINK.
    """

    class Meta:
        name = "pathLinkRefs_RelStructure"

    path_link_ref_or_path_link_ref_by_value: List[
        Union[PathLinkRef, PathLinkRefByValue]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PathLinkRef",
                    "type": PathLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PathLinkRefByValue",
                    "type": PathLinkRefByValue,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
