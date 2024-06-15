from dataclasses import dataclass

from generated.operating_department_ref_structure import (
    OperatingDepartmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatingDepartmentRef(OperatingDepartmentRefStructure):
    """
    Reference to an OPERATING DEPARTMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
