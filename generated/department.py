from dataclasses import dataclass

from generated.department_version_structure import DepartmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Department(DepartmentVersionStructure):
    """
    Department of an ORGANISATION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
