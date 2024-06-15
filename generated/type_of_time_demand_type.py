from dataclasses import dataclass

from generated.type_of_time_demand_type_structure import (
    TypeOfTimeDemandTypeStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfTimeDemandType(TypeOfTimeDemandTypeStructure):
    """
    Classification of a TIME DEMAND TYPE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
