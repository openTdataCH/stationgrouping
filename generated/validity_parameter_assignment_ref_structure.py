from dataclasses import dataclass

from generated.access_right_parameter_assignment_ref_structure import (
    AccessRightParameterAssignmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ValidityParameterAssignmentRefStructure(
    AccessRightParameterAssignmentRefStructure
):
    """
    Type for Reference to a VALIDITY PARAMETER.
    """
