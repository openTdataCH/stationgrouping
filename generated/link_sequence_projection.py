from dataclasses import dataclass

from generated.link_sequence_projection_version_structure import (
    LinkSequenceProjectionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkSequenceProjection(LinkSequenceProjectionVersionStructure):
    """
    A Projection of a whole LINK SEQUENCE as an ordered series of POINTs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
