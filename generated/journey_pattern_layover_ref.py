from dataclasses import dataclass

from generated.journey_pattern_layover_ref_structure import (
    JourneyPatternLayoverRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternLayoverRef(JourneyPatternLayoverRefStructure):
    """
    Reference to a JOURNEY PATTERN LAYOVER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
