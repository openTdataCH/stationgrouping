from dataclasses import dataclass

from generated.group_of_points_version_structure import (
    GroupOfPointsVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfPoints(GroupOfPointsVersionStructure):
    """
    A grouping of POINTs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
