from dataclasses import dataclass

from generated.group_of_entities_ref_structure_1 import (
    GroupOfEntitiesRefStructure1,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfPointsRef2(GroupOfEntitiesRefStructure1):
    """Dummy Reference to a GROUP OF POINTs..

    Workaroudn for XMLspy bug.
    """

    class Meta:
        name = "GroupOfPointsRef_"
        namespace = "http://www.netex.org.uk/netex"
