from dataclasses import dataclass

from generated.schematic_map_member_ref_structure import (
    SchematicMapMemberRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SchematicMapMemberRef(SchematicMapMemberRefStructure):
    """
    Reference to a SCHEMATIC MAP MEMBER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
