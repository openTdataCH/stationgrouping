from dataclasses import dataclass, field

from generated.reserved_space_facility_enumeration import (
    ReservedSpaceFacilityEnumeration,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReservedSpaceFacility:
    """
    Classification of RESERVED SPACE FACILITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: ReservedSpaceFacilityEnumeration = field(
        default=ReservedSpaceFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
