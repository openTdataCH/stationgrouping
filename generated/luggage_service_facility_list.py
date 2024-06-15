from dataclasses import dataclass, field
from typing import List

from generated.luggage_service_facility_enumeration import (
    LuggageServiceFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageServiceFacilityList:
    """
    List of LUGGAGE SERVICE FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[LuggageServiceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
