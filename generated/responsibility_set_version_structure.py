from dataclasses import dataclass, field
from typing import Optional

from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.multilingual_string import MultilingualString
from generated.private_code import PrivateCode
from generated.responsibility_role_assignments_rel_structure import (
    ResponsibilityRoleAssignmentsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResponsibilitySetVersionStructure(DataManagedObjectStructure):
    """Type for a set of RESPONSIBILITY ROLEs that can be associated with a DATA
    MANAGED OBJECT.

    A Child ENTITY has the same responsibilities as its parent.

    :ivar name: Explanation of RESPONSIBILITY SET.
    :ivar private_code:
    :ivar roles: Roles defined by this RESPONSIBILITY SET.
    """

    class Meta:
        name = "ResponsibilitySet_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    roles: Optional[ResponsibilityRoleAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
