from dataclasses import dataclass

from generated.rhythmical_journey_group_ref_structure import (
    RhythmicalJourneyGroupRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RhythmicalJourneyGroupRef(RhythmicalJourneyGroupRefStructure):
    """
    Reference to a RHYTHMICAL JOURNEY GROUP.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
