from dataclasses import dataclass

from generated.sections_in_sequence_rel_structure import (
    LinkSequenceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkSequence(LinkSequenceVersionStructure):
    """
    An LINK SEQUENCE of Links and Nodes.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
