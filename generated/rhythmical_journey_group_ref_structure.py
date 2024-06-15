from dataclasses import dataclass

from generated.journey_frequency_group_ref_structure import (
    JourneyFrequencyGroupRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RhythmicalJourneyGroupRefStructure(JourneyFrequencyGroupRefStructure):
    """
    Type for a reference to a RHYTHMICAL JOURNEY GROUP.
    """
