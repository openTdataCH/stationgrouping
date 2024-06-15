from dataclasses import dataclass, field
from typing import Optional

from generated.version_of_object_ref_structure import (
    VersionOfObjectRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfEntitiesRefStructure2(VersionOfObjectRefStructure):
    """
    Extending Type for a reference to a GROUP OF ENTITies.

    :ivar name_of_member_class: Name of member class if homogeneous.
    """

    class Meta:
        name = "GroupOfEntitiesRefStructure_"

    name_of_member_class: Optional[str] = field(
        default=None,
        metadata={
            "name": "nameOfMemberClass",
            "type": "Attribute",
        },
    )
