from dataclasses import dataclass

from generated.fare_table_row_ref_structure import FareTableRowRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareTableRowRef(FareTableRowRefStructure):
    """
    Reference to a FARE TABLE ROW.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
