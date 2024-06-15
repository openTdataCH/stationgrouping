from dataclasses import dataclass

from generated.operating_department_version_structure import (
    OperatingDepartmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OperatingDepartment(OperatingDepartmentVersionStructure):
    """
    A specific DEPARTMENT which administers certain LINEs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
