from dataclasses import dataclass

from generated.group_of_entities_ref_structure_1 import (
    GroupOfEntitiesRefStructure1,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinesRefStructure(GroupOfEntitiesRefStructure1):
    """
    Type for a GROUP OF LINEs.
    """
