from dataclasses import dataclass

from generated.luggage_allowance_version_structure import (
    LuggageAllowanceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LuggageAllowance(LuggageAllowanceVersionStructure):
    """
    The number and characteristics (weight, volume) of luggage that a holder of an
    access right is entitled to carry.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
