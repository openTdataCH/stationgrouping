from dataclasses import dataclass, field

from generated.retail_facility_enumeration import RetailFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailFacility:
    """
    Classification of RETAIL FACILITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: RetailFacilityEnumeration = field(
        default=RetailFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
