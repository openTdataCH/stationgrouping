from dataclasses import dataclass

from generated.customer_purchase_parameter_assignment_version_structure import (
    CustomerPurchaseParameterAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchaseParameterAssignment(
    CustomerPurchaseParameterAssignmentVersionStructure
):
    """
    A VALIDITY PARAMETER ASSIGNMENT specifying practical parameters for use in a
    CUSTOMER PURCHASE PACKAGE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
