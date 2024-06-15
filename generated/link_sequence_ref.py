from dataclasses import dataclass

from generated.link_sequence_ref_structure import LinkSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkSequenceRef(LinkSequenceRefStructure):
    """
    Reference to a LINK SEQUENCE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
