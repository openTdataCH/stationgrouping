from dataclasses import dataclass

from generated.version_of_object_ref_structure import (
    VersionOfObjectRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfEntitiesRef2(VersionOfObjectRefStructure):
    """
    Reference to a GROUP OF ENTITies.
    """

    class Meta:
        name = "GroupOfEntitiesRef_"
        namespace = "http://www.netex.org.uk/netex"
