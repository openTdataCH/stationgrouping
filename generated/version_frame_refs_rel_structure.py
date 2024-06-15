from dataclasses import dataclass, field
from typing import List, Union

from generated.composite_frame_ref import CompositeFrameRef
from generated.driver_schedule_frame_ref import DriverScheduleFrameRef
from generated.fare_frame_ref import FareFrameRef
from generated.general_frame_ref import GeneralFrameRef
from generated.infrastructure_frame_ref import InfrastructureFrameRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.resource_frame_ref import ResourceFrameRef
from generated.sales_transaction_frame_ref import SalesTransactionFrameRef
from generated.service_calendar_frame_ref import ServiceCalendarFrameRef
from generated.service_frame_ref import ServiceFrameRef
from generated.site_frame_ref import SiteFrameRef
from generated.timetable_frame_ref import TimetableFrameRef
from generated.vehicle_schedule_frame_ref import VehicleScheduleFrameRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VersionFrameRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a VERSION FRAME.
    """

    class Meta:
        name = "versionFrameRefs_RelStructure"

    choice: List[
        Union[
            SalesTransactionFrameRef,
            FareFrameRef,
            ServiceFrameRef,
            DriverScheduleFrameRef,
            VehicleScheduleFrameRef,
            TimetableFrameRef,
            SiteFrameRef,
            InfrastructureFrameRef,
            GeneralFrameRef,
            ResourceFrameRef,
            ServiceCalendarFrameRef,
            CompositeFrameRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SalesTransactionFrameRef",
                    "type": SalesTransactionFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareFrameRef",
                    "type": FareFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFrameRef",
                    "type": ServiceFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverScheduleFrameRef",
                    "type": DriverScheduleFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleScheduleFrameRef",
                    "type": VehicleScheduleFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetableFrameRef",
                    "type": TimetableFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFrameRef",
                    "type": SiteFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InfrastructureFrameRef",
                    "type": InfrastructureFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralFrameRef",
                    "type": GeneralFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResourceFrameRef",
                    "type": ResourceFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendarFrameRef",
                    "type": ServiceCalendarFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompositeFrameRef",
                    "type": CompositeFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
