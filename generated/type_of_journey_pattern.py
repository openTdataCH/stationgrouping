from dataclasses import dataclass

from generated.type_of_journey_pattern_value_structure import (
    TypeOfJourneyPatternValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfJourneyPattern(TypeOfJourneyPatternValueStructure):
    """
    A classification of JOURNEY PATTERNs according to their functional purpose.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
