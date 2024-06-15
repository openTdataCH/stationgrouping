from dataclasses import dataclass

from generated.schematic_map_ref_structure import SchematicMapRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SchematicMapRef(SchematicMapRefStructure):
    """
    Reference to a SCHEMATIC MAP.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
