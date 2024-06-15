from dataclasses import dataclass, field
from typing import Optional

from generated.organisation_part_version_structure import (
    OrganisationPartVersionStructure,
)
from generated.organisational_unit_refs_rel_structure import (
    OrganisationalUnitRefsRelStructure,
)
from generated.type_of_operation_ref import TypeOfOperationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DepartmentVersionStructure(OrganisationPartVersionStructure):
    """
    Type for a DEPARTMENT.

    :ivar type_of_operation_ref:
    :ivar units: Name of DEPARTMENT.
    """

    class Meta:
        name = "Department_VersionStructure"

    type_of_operation_ref: Optional[TypeOfOperationRef] = field(
        default=None,
        metadata={
            "name": "TypeOfOperationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    units: Optional[OrganisationalUnitRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
