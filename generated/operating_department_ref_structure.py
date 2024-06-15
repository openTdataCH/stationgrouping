from dataclasses import dataclass

from generated.department_ref_structure import DepartmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatingDepartmentRefStructure(DepartmentRefStructure):
    """
    Type for a reference to an OPERATING DEPARTMENT.
    """
