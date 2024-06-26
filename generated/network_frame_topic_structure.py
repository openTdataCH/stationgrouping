from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDateTime

from generated.closed_timestamp_range_structure import (
    ClosedTimestampRangeStructure,
)
from generated.composite_frame_ref import CompositeFrameRef
from generated.driver_schedule_frame_ref import DriverScheduleFrameRef
from generated.empty_type_2 import EmptyType2
from generated.entity_in_version_structure import (
    AvailabilityCondition,
    SimpleAvailabilityCondition,
    ValidDuring,
    ValidityCondition,
    ValidityRuleParameter,
    ValidityTrigger,
)
from generated.fare_frame_ref import FareFrameRef
from generated.general_frame_ref import GeneralFrameRef
from generated.infrastructure_frame_ref import InfrastructureFrameRef
from generated.network_filter_by_value_structure import (
    NetworkFilterByValueStructure,
)
from generated.resource_frame_ref import ResourceFrameRef
from generated.sales_transaction_frame_ref import SalesTransactionFrameRef
from generated.service_calendar_frame_ref import ServiceCalendarFrameRef
from generated.service_frame_ref import ServiceFrameRef
from generated.site_frame_ref import SiteFrameRef
from generated.timetable_frame_ref import TimetableFrameRef
from generated.topic_structure import TopicStructure
from generated.type_of_frame_ref import TypeOfFrameRef
from generated.vehicle_schedule_frame_ref import VehicleScheduleFrameRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkFrameTopicStructure(TopicStructure):
    """
    Type for a Data Object Filter Topic.
    """

    choice: Optional[
        Union[
            EmptyType2,
            "NetworkFrameTopicStructure.ChangedSince",
            "NetworkFrameTopicStructure.CurrentAt",
            ClosedTimestampRangeStructure,
            "NetworkFrameTopicStructure.SelectionValidityConditions",
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "Current",
                    "type": EmptyType2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChangedSince",
                    "type": ForwardRef(
                        "NetworkFrameTopicStructure.ChangedSince"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CurrentAt",
                    "type": ForwardRef("NetworkFrameTopicStructure.CurrentAt"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HistoricBetween",
                    "type": ClosedTimestampRangeStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "selectionValidityConditions",
                    "type": ForwardRef(
                        "NetworkFrameTopicStructure.SelectionValidityConditions"
                    ),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_frame_ref: Optional[TypeOfFrameRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice_1: List[
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
            NetworkFilterByValueStructure,
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
                {
                    "name": "NetworkFilterByValue",
                    "type": NetworkFilterByValueStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class SelectionValidityConditions:
        choice: List[
            Union[
                SimpleAvailabilityCondition,
                ValidDuring,
                AvailabilityCondition,
                ValidityRuleParameter,
                ValidityTrigger,
                ValidityCondition,
            ]
        ] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "SimpleAvailabilityCondition",
                        "type": SimpleAvailabilityCondition,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ValidDuring",
                        "type": ValidDuring,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "AvailabilityCondition",
                        "type": AvailabilityCondition,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ValidityRuleParameter",
                        "type": ValidityRuleParameter,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ValidityTrigger",
                        "type": ValidityTrigger,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                    {
                        "name": "ValidityCondition",
                        "type": ValidityCondition,
                        "namespace": "http://www.netex.org.uk/netex",
                    },
                ),
            },
        )

    @dataclass(kw_only=True)
    class ChangedSince:
        value: XmlDateTime = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class CurrentAt:
        value: XmlDateTime = field(
            metadata={
                "required": True,
            }
        )
