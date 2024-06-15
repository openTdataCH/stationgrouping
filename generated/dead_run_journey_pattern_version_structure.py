from dataclasses import dataclass

from generated.sections_in_sequence_rel_structure import (
    JourneyPatternVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeadRunJourneyPatternVersionStructure(JourneyPatternVersionStructure):
    """
    Type for DEAD RUN JOURNEY PATTERN.
    """

    class Meta:
        name = "DeadRunJourneyPattern_VersionStructure"
