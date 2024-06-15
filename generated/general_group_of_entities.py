from dataclasses import dataclass

from generated.general_group_of_entities_version_structure import (
    GeneralGroupOfEntitiesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralGroupOfEntities(GeneralGroupOfEntitiesVersionStructure):
    """
    A grouping of ENTITies which will be commonly referenced for a specific
    purpose.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
