from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.open_transport_mode_ref import OpenTransportModeRef
from generated.transport_mode_structure import TransportModeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportModesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TRANSPORT MODEs.
    """

    class Meta:
        name = "transportModes_RelStructure"

    open_transport_mode_ref_or_transport_mode: List[
        Union[OpenTransportModeRef, TransportModeStructure]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OpenTransportModeRef",
                    "type": OpenTransportModeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportMode",
                    "type": TransportModeStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
