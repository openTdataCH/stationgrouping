from dataclasses import dataclass

from generated.sections_in_sequence_rel_structure import (
    LinkSequenceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternAbstract(LinkSequenceVersionStructure):
    """
    Dummy Supertype for JOURNEY PATTERN.
    """

    class Meta:
        name = "JourneyPattern_"
        namespace = "http://www.netex.org.uk/netex"
