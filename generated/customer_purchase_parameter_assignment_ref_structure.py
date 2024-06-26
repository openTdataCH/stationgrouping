from dataclasses import dataclass

from generated.validity_parameter_assignment_ref_structure import (
    ValidityParameterAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerPurchaseParameterAssignmentRefStructure(
    ValidityParameterAssignmentRefStructure
):
    """
    Type for Reference to a CUSTOMER PURCHASE PARAMETER.
    """
