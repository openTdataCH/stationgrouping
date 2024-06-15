from dataclasses import dataclass, field

from generated.money_facility_enumeration import MoneyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MoneyFacility:
    """
    Classification of MONEY FACILITY.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MoneyFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
