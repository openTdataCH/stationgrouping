from dataclasses import dataclass

from generated.type_of_time_demand_type_ref_structure import (
    TypeOfTimeDemandTypeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfTimeDemandTypeRef(TypeOfTimeDemandTypeRefStructure):
    """
    Reference to a TYPE OF TIME DEMAND TYPE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
