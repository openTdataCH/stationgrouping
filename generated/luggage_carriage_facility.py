from dataclasses import dataclass, field

from generated.luggage_carriage_enumeration import LuggageCarriageEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageCarriageFacility:
    """
    Classification of LUGGAGE CARRIAGE FACILITY type.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: LuggageCarriageEnumeration = field(
        default=LuggageCarriageEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
