from dataclasses import dataclass

from generated.fare_table_column_ref_structure import (
    FareTableColumnRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareTableColumnRef(FareTableColumnRefStructure):
    """
    Reference to a FARE TABLE COLUMN.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
