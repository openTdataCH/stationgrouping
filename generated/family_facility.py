from dataclasses import dataclass, field

from generated.family_facility_enumeration import FamilyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FamilyFacility:
    """
    Classification of FAMILY FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: FamilyFacilityEnumeration = field(
        default=FamilyFacilityEnumeration.NONE,
        metadata={
            "required": True,
        },
    )
