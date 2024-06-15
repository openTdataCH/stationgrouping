from dataclasses import dataclass, field
from typing import List, Union

from generated.frame_containment_structure import FrameContainmentStructure
from generated.priceable_object_version_structure import (
    FareTable,
    FareTableInContext,
)
from generated.standard_fare_table import StandardFareTable

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareTablesInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of TARIFF.
    """

    class Meta:
        name = "fareTablesInFrame_RelStructure"

    standard_fare_table_or_fare_table_in_context_or_fare_table: List[
        Union[StandardFareTable, FareTableInContext, FareTable]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StandardFareTable",
                    "type": StandardFareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTableInContext",
                    "type": FareTableInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareTable",
                    "type": FareTable,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
