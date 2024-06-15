from dataclasses import dataclass, field
from typing import Optional

from generated.group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from generated.point_refs_rel_structure import PointRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfPointsVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for GROUP OF POINTs.

    :ivar members: POINTs in GROUP OF POINTs.
    """

    class Meta:
        name = "GroupOfPoints_VersionStructure"

    members: Optional[PointRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
