from dataclasses import dataclass, field
from typing import Optional, Union

from generated.assignment_version_structure_1 import (
    AssignmentVersionStructure1,
)
from generated.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from generated.private_code import PrivateCode
from generated.scheduled_stop_point import ScheduledStopPoint
from generated.scheduled_stop_point_ref import ScheduledStopPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopAssignmentVersionStructure(AssignmentVersionStructure1):
    """
    Type for a STOP ASSIGNMENT.

    :ivar boarding_use: Whether alignment is for boarding use. Default
        is 'true'.
    :ivar alighting_use: Whether alignment is for alighting use. Default
        is 'true'.
    :ivar private_code:
    :ivar
        fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point:
    """

    class Meta:
        name = "StopAssignment_VersionStructure"

    boarding_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BoardingUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alighting_use: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AlightingUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref_or_scheduled_stop_point: Optional[
        Union[
            FareScheduledStopPointRef,
            ScheduledStopPointRef,
            ScheduledStopPoint,
        ]
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
                {
                    "name": "ScheduledStopPoint",
                    "type": ScheduledStopPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
