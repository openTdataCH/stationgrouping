from dataclasses import dataclass

from generated.group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfEntities(GroupOfEntitiesVersionStructure):
    """
    A grouping of ENTITies which will be commonly referenced for a specific
    purpose.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
