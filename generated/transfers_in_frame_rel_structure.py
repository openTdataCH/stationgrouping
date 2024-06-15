from dataclasses import dataclass, field
from typing import List, Union

from generated.access import Access
from generated.connection import Connection
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.default_connection import DefaultConnection
from generated.site_connection import SiteConnection

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransfersInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of CONNECTIONs.
    """

    class Meta:
        name = "transfersInFrame_RelStructure"

    choice: List[
        Union[Connection, DefaultConnection, SiteConnection, Access]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Connection",
                    "type": Connection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DefaultConnection",
                    "type": DefaultConnection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteConnection",
                    "type": SiteConnection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Access",
                    "type": Access,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
