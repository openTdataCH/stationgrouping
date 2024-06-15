from dataclasses import dataclass

from generated.journey_pattern_ref_structure import JourneyPatternRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyPatternRefStructure(JourneyPatternRefStructure):
    """
    Type for a reference to a SERVICE JOURNEY PATTERN.
    """
