from dataclasses import dataclass, field
from typing import List, Union

from generated.access_right_parameter_assignment import (
    AccessRightParameterAssignment,
)
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.customer_purchase_parameter_assignment import (
    CustomerPurchaseParameterAssignment,
)
from generated.generic_parameter_assignments_rel_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
)
from generated.specific_parameter_assignments_rel_structure import (
    SpecificParameterAssignment,
)
from generated.validity_parameter_assignment import ValidityParameterAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessRightParameterAssignmentsRelStructure(
    ContainmentAggregationStructure
):
    """
    Type for a list of FARE ACCESS RIGHT PARAMETERs.
    """

    class Meta:
        name = "accessRightParameterAssignments_RelStructure"

    choice: List[
        Union[
            CustomerPurchaseParameterAssignment,
            SpecificParameterAssignment,
            GenericParameterAssignmentInContext,
            GenericParameterAssignment,
            ValidityParameterAssignment,
            AccessRightParameterAssignment,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchaseParameterAssignment",
                    "type": CustomerPurchaseParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecificParameterAssignment",
                    "type": SpecificParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": GenericParameterAssignmentInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignment",
                    "type": GenericParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidityParameterAssignment",
                    "type": ValidityParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightParameterAssignment",
                    "type": AccessRightParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
