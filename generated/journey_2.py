from dataclasses import dataclass

from generated.sections_in_sequence_rel_structure import (
    LinkSequenceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Journey2(LinkSequenceVersionStructure):
    """
    Dummy supertype for Journey.
    """

    class Meta:
        name = "Journey_"
        namespace = "http://www.netex.org.uk/netex"
