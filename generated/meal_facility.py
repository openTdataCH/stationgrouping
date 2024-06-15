from dataclasses import dataclass, field

from generated.meal_facility_enumeration import MealFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MealFacility:
    """
    Classification of MEAL FACILITY type.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MealFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
