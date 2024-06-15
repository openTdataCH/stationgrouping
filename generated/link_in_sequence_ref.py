from dataclasses import dataclass

from generated.link_in_sequence_ref_structure import LinkInSequenceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkInSequenceRef(LinkInSequenceRefStructure):
    """
    Reference to a LINK IN SEQUENCE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
