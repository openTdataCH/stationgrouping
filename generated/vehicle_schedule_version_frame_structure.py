from dataclasses import dataclass, field
from typing import Optional

from generated.blocks_in_frame_rel_structure import BlocksInFrameRelStructure
from generated.common_version_frame_structure import (
    CommonVersionFrameStructure,
)
from generated.courses_of_journeys_in_frame_rel_structure import (
    CoursesOfJourneysInFrameRelStructure,
)
from generated.relief_opportunities_in_frame_rel_structure import (
    ReliefOpportunitiesInFrameRelStructure,
)
from generated.service_calendar_frame_ref import ServiceCalendarFrameRef
from generated.vehicle_services_in_frame_rel_structure import (
    VehicleServicesInFrameRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleScheduleVersionFrameStructure(CommonVersionFrameStructure):
    """
    Type for a VEHICLE SCHEDULE FRAME.

    :ivar service_calendar_frame_ref:
    :ivar blocks: BLOCKs in frame.
    :ivar courses_of_journeys: COURSE OF JOURNEYs (Runs) in frame.
    :ivar vehicle_services: VEHICLE SERVICES in frame.
    :ivar relief_opportunities: VEHICLE SERVICES in frame.
    """

    class Meta:
        name = "VehicleSchedule_VersionFrameStructure"

    service_calendar_frame_ref: Optional[ServiceCalendarFrameRef] = field(
        default=None,
        metadata={
            "name": "ServiceCalendarFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    blocks: Optional[BlocksInFrameRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    courses_of_journeys: Optional[CoursesOfJourneysInFrameRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "coursesOfJourneys",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    vehicle_services: Optional[VehicleServicesInFrameRelStructure] = field(
        default=None,
        metadata={
            "name": "vehicleServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    relief_opportunities: Optional[ReliefOpportunitiesInFrameRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "reliefOpportunities",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
