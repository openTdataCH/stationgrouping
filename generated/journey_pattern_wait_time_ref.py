from dataclasses import dataclass

from generated.journey_pattern_run_time_ref_structure import (
    JourneyPatternRunTimeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternWaitTimeRef(JourneyPatternRunTimeRefStructure):
    """
    Reference to a JOURNEY PATTERN WAIT TIME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
