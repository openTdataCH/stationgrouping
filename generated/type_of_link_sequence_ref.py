from dataclasses import dataclass

from generated.type_of_link_sequence_ref_structure import (
    TypeOfLinkSequenceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfLinkSequenceRef(TypeOfLinkSequenceRefStructure):
    """
    Reference to a TYPE OF LINK SEQUENCE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
