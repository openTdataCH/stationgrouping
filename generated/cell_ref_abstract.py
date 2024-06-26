from dataclasses import dataclass

from generated.version_of_object_ref_structure import (
    VersionOfObjectRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CellRefAbstract(VersionOfObjectRefStructure):
    """
    Dummy Reference to a FARE TABLE CELL.
    """

    class Meta:
        name = "CellRef_"
        namespace = "http://www.netex.org.uk/netex"
