from dataclasses import dataclass

from generated.schematic_map_version_structure import (
    SchematicMapVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SchematicMap(SchematicMapVersionStructure):
    """
    A projection of a set of ENTITies onto a bitmap image so as to support
    hyperlinked interactions.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
