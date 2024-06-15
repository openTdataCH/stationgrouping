from dataclasses import dataclass, field
from typing import Optional, Union

from generated.assignment_version_structure_1 import (
    AssignmentVersionStructure1,
)
from generated.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from generated.direction_ref import DirectionRef
from generated.display_assignment_type_enumeration import (
    DisplayAssignmentTypeEnumeration,
)
from generated.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from generated.flexible_line_ref import FlexibleLineRef
from generated.journey_pattern_ref import JourneyPatternRef
from generated.line_ref import LineRef
from generated.logical_display_ref import LogicalDisplayRef
from generated.scheduled_stop_point_ref import ScheduledStopPointRef
from generated.service_journey_pattern_ref import ServiceJourneyPatternRef
from generated.service_pattern_ref import ServicePatternRef
from generated.vehicle_mode import VehicleMode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DisplayAssignmentVersionStructure(AssignmentVersionStructure1):
    """
    Type for a DISPLAY ASSIGNMENT.

    :ivar logical_display_ref:
    :ivar fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref:
    :ivar vehicle_mode:
    :ivar flexible_line_ref_or_line_ref:
    :ivar direction_ref:
    :ivar choice:
    :ivar display_assignment_type: Type of data to display.
    :ivar number_of_journeys_to_show: Number of journeys to show,
        default is all.
    :ivar display_priority: Relative priority of display assignment, vis
        a vis other assignments
    """

    class Meta:
        name = "DisplayAssignment_VersionStructure"

    logical_display_ref: Optional[LogicalDisplayRef] = field(
        default=None,
        metadata={
            "name": "LogicalDisplayRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref: Optional[
        Union[FareScheduledStopPointRef, ScheduledStopPointRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    vehicle_mode: Optional[VehicleMode] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flexible_line_ref_or_line_ref: Optional[
        Union[FlexibleLineRef, LineRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            ServiceJourneyPatternRef,
            ServicePatternRef,
            DeadRunJourneyPatternRef,
            JourneyPatternRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceJourneyPatternRef",
                    "type": ServiceJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicePatternRef",
                    "type": ServicePatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRunJourneyPatternRef",
                    "type": DeadRunJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPatternRef",
                    "type": JourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    display_assignment_type: Optional[DisplayAssignmentTypeEnumeration] = (
        field(
            default=None,
            metadata={
                "name": "DisplayAssignmentType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    number_of_journeys_to_show: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfJourneysToShow",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    display_priority: Optional[int] = field(
        default=None,
        metadata={
            "name": "DisplayPriority",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
