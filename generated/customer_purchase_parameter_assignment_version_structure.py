from dataclasses import dataclass

from generated.validity_parameter_assignment_version_structure import (
    ValidityParameterAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchaseParameterAssignmentVersionStructure(
    ValidityParameterAssignmentVersionStructure
):
    """
    Type for CustomerPurchase PARAMETER ASSIGNMENT.
    """

    class Meta:
        name = "CustomerPurchaseParameterAssignment_VersionStructure"
