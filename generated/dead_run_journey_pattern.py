from dataclasses import dataclass

from generated.dead_run_journey_pattern_version_structure import (
    DeadRunJourneyPatternVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeadRunJourneyPattern(DeadRunJourneyPatternVersionStructure):
    """
    A JOURNEY PATTERN to be used for DEAD RUNs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
