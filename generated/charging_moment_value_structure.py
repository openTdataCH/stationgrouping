from dataclasses import dataclass

from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ChargingMomentValueStructure(TypeOfValueVersionStructure):
    """
    Type for a CHARGING MOMENT.
    """

    class Meta:
        name = "ChargingMoment_ValueStructure"
