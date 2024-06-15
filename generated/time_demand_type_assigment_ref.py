from dataclasses import dataclass

from generated.time_demand_type_assigment_ref_structure import (
    TimeDemandTypeAssigmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeDemandTypeAssigmentRef(TimeDemandTypeAssigmentRefStructure):
    """
    Reference to a TIME DEMAND ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
