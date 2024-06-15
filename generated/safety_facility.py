from dataclasses import dataclass, field

from generated.safety_facility_enumeration import SafetyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SafetyFacility:
    """Classification of SAFETY FACILITY type - TPEG pti23."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: SafetyFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
