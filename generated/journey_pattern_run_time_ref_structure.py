from dataclasses import dataclass

from generated.journey_timing_ref_structure import JourneyTimingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPatternRunTimeRefStructure(JourneyTimingRefStructure):
    """
    Type for a reference to a JOURNEY PATTERN RUN TIME.
    """
