from dataclasses import dataclass

from generated.department_ref_structure import DepartmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DepartmentRef(DepartmentRefStructure):
    """
    Reference to a DEPARTMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
