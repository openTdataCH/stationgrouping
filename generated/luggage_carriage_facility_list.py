from dataclasses import dataclass, field
from typing import List

from generated.luggage_carriage_enumeration import LuggageCarriageEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageCarriageFacilityList:
    """
    List of LUGGAGE CARRIAGE FACILITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[LuggageCarriageEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
