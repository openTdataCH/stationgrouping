from dataclasses import dataclass, field

from generated.medical_facility_enumeration import MedicalFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MedicalFacility:
    """Classification of MEDICAL FACILITY type - TPEG pti23."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MedicalFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
