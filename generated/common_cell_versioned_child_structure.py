from dataclasses import dataclass, field
from typing import Optional, Union

from generated.entity_in_version_structure import VersionedChildStructure
from generated.fare_table_column_ref_structure import (
    FareTableColumnRefStructure,
)
from generated.fare_table_ref import FareTableRef
from generated.fare_table_row_ref_structure import FareTableRowRefStructure
from generated.multilingual_string import MultilingualString
from generated.standard_fare_table_ref import StandardFareTableRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommonCellVersionedChildStructure(VersionedChildStructure):
    """
    Type for a CELL.

    :ivar name: Name of CELL.
    :ivar description: Description of CELL.
    :ivar standard_fare_table_ref_or_fare_table_ref:
    :ivar column_ref: Column for CELL.
    :ivar row_ref: Row for CELL.
    :ivar order: Order in which cell is to appear.
    """

    class Meta:
        name = "CommonCell_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    standard_fare_table_ref_or_fare_table_ref: Optional[
        Union[StandardFareTableRef, FareTableRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StandardFareTableRef",
                    "type": StandardFareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableRef",
                    "type": FareTableRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    column_ref: Optional[FareTableColumnRefStructure] = field(
        default=None,
        metadata={
            "name": "ColumnRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    row_ref: Optional[FareTableRowRefStructure] = field(
        default=None,
        metadata={
            "name": "RowRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
