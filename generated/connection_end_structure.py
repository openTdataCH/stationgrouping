from dataclasses import dataclass, field
from typing import Optional

from generated.all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from generated.scheduled_stop_point_ref_structure import (
    ScheduledStopPointRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ConnectionEndStructure:
    """
    Type for a CONNECTION END.

    :ivar transport_mode: MODE of end Point of CONNECTION. Default is
        all modes. Can be derived.
    :ivar scheduled_stop_point_ref: Identifier of  specific SCHEDULED
        STOP POINT at end of CONNECTION.
    """

    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    scheduled_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
