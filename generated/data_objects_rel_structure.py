from dataclasses import dataclass, field
from typing import List, Union

from generated.driver_schedule_frame import DriverScheduleFrame
from generated.fare_frame import FareFrame
from generated.general_version_frame_structure import (
    CompositeFrame,
    GeneralFrame,
)
from generated.infrastructure_frame import InfrastructureFrame
from generated.resource_frame import ResourceFrame
from generated.sales_transaction_frame import SalesTransactionFrame
from generated.service_calendar_frame import ServiceCalendarFrame
from generated.service_frame import ServiceFrame
from generated.site_frame import SiteFrame
from generated.timetable_frame import TimetableFrame
from generated.vehicle_schedule_frame import VehicleScheduleFrame

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectsRelStructure:
    """
    Type for a list of objects.
    """

    class Meta:
        name = "dataObjects_RelStructure"

    choice: List[
        Union[
            CompositeFrame,
            SalesTransactionFrame,
            FareFrame,
            DriverScheduleFrame,
            VehicleScheduleFrame,
            ServiceFrame,
            TimetableFrame,
            SiteFrame,
            InfrastructureFrame,
            GeneralFrame,
            ResourceFrame,
            ServiceCalendarFrame,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompositeFrame",
                    "type": CompositeFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesTransactionFrame",
                    "type": SalesTransactionFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareFrame",
                    "type": FareFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DriverScheduleFrame",
                    "type": DriverScheduleFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleScheduleFrame",
                    "type": VehicleScheduleFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceFrame",
                    "type": ServiceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimetableFrame",
                    "type": TimetableFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFrame",
                    "type": SiteFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InfrastructureFrame",
                    "type": InfrastructureFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralFrame",
                    "type": GeneralFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResourceFrame",
                    "type": ResourceFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceCalendarFrame",
                    "type": ServiceCalendarFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
