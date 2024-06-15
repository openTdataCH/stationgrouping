from dataclasses import dataclass

from generated.group_of_points_ref_structure import GroupOfPointsRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfPointsRef1(GroupOfPointsRefStructure):
    """
    Reference to a GROUP OF POINTs.
    """

    class Meta:
        name = "GroupOfPointsRef"
        namespace = "http://www.netex.org.uk/netex"
