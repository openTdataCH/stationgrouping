from dataclasses import dataclass

from generated.fare_point_in_pattern_versioned_child_structure import (
    FarePointInPatternVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FarePointInPattern(FarePointInPatternVersionedChildStructure):
    """
    A POINT IN PATTERN which represents the start or end of a FARE SECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
