from dataclasses import dataclass, field

from generated.luggage_service_facility_enumeration import (
    LuggageServiceFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageServiceFacility:
    """
    Classification of LUGGAGE SERVICE FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: LuggageServiceFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
