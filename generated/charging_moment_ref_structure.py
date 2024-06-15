from dataclasses import dataclass

from generated.type_of_value_ref_structure import TypeOfValueRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingMomentRefStructure(TypeOfValueRefStructure):
    """Type for a CHARGING MOMENT.

    +v1.1
    """
