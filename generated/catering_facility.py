from dataclasses import dataclass, field

from generated.catering_facility_enumeration import CateringFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CateringFacility:
    """Classification of CATERING FACILITY type - TPEG pti23."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: CateringFacilityEnumeration = field(
        default=CateringFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
