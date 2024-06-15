from dataclasses import dataclass, field
from typing import Optional

from generated.link_version_structure import LinkVersionStructure
from generated.operational_context_ref import OperationalContextRef
from generated.scheduled_stop_point_ref_structure import (
    ScheduledStopPointRefStructure,
)
from generated.vehicle_mode import VehicleMode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceLinkVersionStructure(LinkVersionStructure):
    """
    Type for SERVICE LINK.

    :ivar from_point_ref: Identifier of SCHEDULED STOP POINT from which
        Link starts.
    :ivar to_point_ref: Identifier of SCHEDULED STOP POINT at which Link
        ends.
    :ivar vehicle_mode:
    :ivar operational_context_ref:
    """

    class Meta:
        name = "ServiceLink_VersionStructure"

    from_point_ref: ScheduledStopPointRefStructure = field(
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_point_ref: ScheduledStopPointRefStructure = field(
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    vehicle_mode: Optional[VehicleMode] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operational_context_ref: Optional[OperationalContextRef] = field(
        default=None,
        metadata={
            "name": "OperationalContextRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
