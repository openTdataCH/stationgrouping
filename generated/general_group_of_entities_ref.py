from dataclasses import dataclass

from generated.general_group_of_entities_ref_structure import (
    GeneralGroupOfEntitiesRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GeneralGroupOfEntitiesRef(GeneralGroupOfEntitiesRefStructure):
    """
    Reference to a GENERAL GROUP OF ENTITies.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
