from dataclasses import dataclass

from generated.cell_ref_structure import CellRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CellRef(CellRefStructure):
    """
    Reference to a CELL.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
