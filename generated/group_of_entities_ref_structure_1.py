from dataclasses import dataclass

from generated.group_of_entities_ref_structure_2 import (
    GroupOfEntitiesRefStructure2,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfEntitiesRefStructure1(GroupOfEntitiesRefStructure2):
    """
    Extending Type for a reference to a GROUP OF ENTITies.
    """

    class Meta:
        name = "GroupOfEntitiesRefStructure"
