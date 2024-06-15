from dataclasses import dataclass

from generated.luggage_allowance_ref_structure import (
    LuggageAllowanceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageAllowanceRef(LuggageAllowanceRefStructure):
    """
    Reference to a LUGGAGE ALLOWANCE PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
