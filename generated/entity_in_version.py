from dataclasses import dataclass

from generated.entity_in_version_structure import EntityInVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntityInVersion(EntityInVersionStructure):
    """The ENTITies associated to a given VERSION.

    ENTITY IN VERSION is restricted by ENTITY IN FRAME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
