from dataclasses import dataclass

from generated.sections_in_sequence_rel_structure import (
    LinkSequenceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Section2(LinkSequenceVersionStructure):
    """
    Dummy Supertype for SECTION  +v1.1.
    """

    class Meta:
        name = "Section_"
        namespace = "http://www.netex.org.uk/netex"
