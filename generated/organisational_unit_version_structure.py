from dataclasses import dataclass, field
from typing import Optional

from generated.department_ref import DepartmentRef
from generated.organisation_part_version_structure import (
    OrganisationPartVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationalUnitVersionStructure(OrganisationPartVersionStructure):
    """
    Type for a ORGANISATIONAL UNIT.
    """

    class Meta:
        name = "OrganisationalUnit_VersionStructure"

    department_ref: Optional[DepartmentRef] = field(
        default=None,
        metadata={
            "name": "DepartmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
