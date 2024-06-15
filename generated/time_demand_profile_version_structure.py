from dataclasses import dataclass, field
from typing import Optional, Union

from generated.dead_run_journey_pattern_ref import DeadRunJourneyPatternRef
from generated.dead_run_ref import DeadRunRef
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.journey_pattern_ref import JourneyPatternRef
from generated.multilingual_string import MultilingualString
from generated.service_journey_pattern_ref import ServiceJourneyPatternRef
from generated.service_pattern_ref import ServicePatternRef
from generated.time_demand_profile_members_rel_structure import (
    TimeDemandProfileMembersRelStructure,
)
from generated.time_demand_type_ref import TimeDemandTypeRef
from generated.timeband_ref import TimebandRef
from generated.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeDemandProfileVersionStructure(DataManagedObjectStructure):
    """
    Type for TIME DEMAND PROFILE.

    :ivar name: Name of Profile.
    :ivar time_demand_type_ref_or_timeband_ref:
    :ivar choice:
    :ivar dead_run_ref_or_vehicle_journey_ref:
    :ivar members:
    """

    class Meta:
        name = "TimeDemandProfile_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_demand_type_ref_or_timeband_ref: Optional[
        Union[TimeDemandTypeRef, TimebandRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TimeDemandTypeRef",
                    "type": TimeDemandTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimebandRef",
                    "type": TimebandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
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
    dead_run_ref_or_vehicle_journey_ref: Optional[
        Union[DeadRunRef, VehicleJourneyRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DeadRunRef",
                    "type": DeadRunRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    members: Optional[TimeDemandProfileMembersRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
