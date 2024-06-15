from dataclasses import dataclass

from generated.version_of_object_ref_structure import (
    VersionOfObjectRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CellRefStructure(VersionOfObjectRefStructure):
    """
    Type for Reference to a CELL.
    """
