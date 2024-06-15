from dataclasses import dataclass

from generated.path_link_in_sequence_ref_structure import (
    PathLinkInSequenceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkInSequenceRef(PathLinkInSequenceRefStructure):
    """Reference to a PATH LINK IN SEQUENCE.

    If given by context does not need to be stated.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
