from dataclasses import dataclass, field
from typing import Optional, Union

from generated.flexible_area_ref import FlexibleAreaRef
from generated.flexible_quay_ref import FlexibleQuayRef
from generated.flexible_stop_place_ref import FlexibleStopPlaceRef
from generated.hail_and_ride_area_ref import HailAndRideAreaRef
from generated.stop_assignment_version_structure import (
    StopAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleStopAssignmentVersionStructure(StopAssignmentVersionStructure):
    """
    Type for a FLEXIBLE STOP ASSIGNMENT.
    """

    class Meta:
        name = "FlexibleStopAssignment_VersionStructure"

    flexible_stop_place_ref: FlexibleStopPlaceRef = field(
        metadata={
            "name": "FlexibleStopPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    hail_and_ride_area_ref_or_flexible_area_ref_or_flexible_quay_ref: Optional[
        Union[HailAndRideAreaRef, FlexibleAreaRef, FlexibleQuayRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "HailAndRideAreaRef",
                    "type": HailAndRideAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleAreaRef",
                    "type": FlexibleAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleQuayRef",
                    "type": FlexibleQuayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
