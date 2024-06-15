from dataclasses import dataclass, field

from generated.sanitary_facility_enumeration import SanitaryFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SanitaryFacility:
    """Classification of Sanitary FACILITY type - TPEG pti23."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: SanitaryFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
