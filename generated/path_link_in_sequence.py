from dataclasses import dataclass

from generated.path_link_in_sequence_versioned_child_structure import (
    PathLinkInSequenceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkInSequence(PathLinkInSequenceVersionedChildStructure):
    """
    A step in a Navigation PATH.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
