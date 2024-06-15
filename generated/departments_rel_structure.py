from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.department import Department
from generated.department_ref import DepartmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DepartmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of DEPARTMENTs.
    """

    class Meta:
        name = "departments_RelStructure"

    department_ref_or_department: List[Union[DepartmentRef, Department]] = (
        field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "DepartmentRef",
                        "type": DepartmentRef,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "Department",
                        "type": Department,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )
    )
