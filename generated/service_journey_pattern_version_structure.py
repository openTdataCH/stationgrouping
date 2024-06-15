from dataclasses import dataclass, field
from typing import Optional

from generated.sections_in_sequence_rel_structure import (
    JourneyPatternVersionStructure,
)
from generated.service_journey_pattern_type_enumeration import (
    ServiceJourneyPatternTypeEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceJourneyPatternVersionStructure(JourneyPatternVersionStructure):
    """
    Type for SERVICE JOURNEY PATTERN.

    :ivar service_journey_pattern_type: Type of SERVICE JOURNEY PATTERN.
    """

    class Meta:
        name = "ServiceJourneyPattern_VersionStructure"

    service_journey_pattern_type: Optional[
        ServiceJourneyPatternTypeEnumeration
    ] = field(
        default=None,
        metadata={
            "name": "ServiceJourneyPatternType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
