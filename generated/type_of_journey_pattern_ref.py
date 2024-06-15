from dataclasses import dataclass

from generated.type_of_journey_pattern_ref_structure import (
    TypeOfJourneyPatternRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfJourneyPatternRef(TypeOfJourneyPatternRefStructure):
    """
    Reference to a TYPE OF JOURNEY PATTERN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
