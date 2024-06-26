from dataclasses import dataclass

from generated.group_of_entities_ref_structure_1 import (
    GroupOfEntitiesRefStructure1,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfEntitiesRef1(GroupOfEntitiesRefStructure1):
    """
    Reference to a GROUP OF ENTITies.
    """

    class Meta:
        name = "GroupOfEntitiesRef"
        namespace = "http://www.netex.org.uk/netex"
