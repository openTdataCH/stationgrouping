from dataclasses import dataclass, field
from typing import Optional, Union

from generated.dated_special_service_ref import DatedSpecialServiceRef
from generated.dated_vehicle_journey_ref import DatedVehicleJourneyRef
from generated.dead_run_ref import DeadRunRef
from generated.entity_in_version_structure import VersionedChildStructure
from generated.fare_point_in_pattern_ref import FarePointInPatternRef
from generated.point_in_journey_pattern_ref import PointInJourneyPatternRef
from generated.service_journey_ref import ServiceJourneyRef
from generated.special_service_ref import SpecialServiceRef
from generated.stop_point_in_journey_pattern_ref import (
    StopPointInJourneyPatternRef,
)
from generated.template_service_journey_ref import TemplateServiceJourneyRef
from generated.timing_point_in_journey_pattern_ref import (
    TimingPointInJourneyPatternRef,
)
from generated.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassingTimeVersionedChildStructure(VersionedChildStructure):
    """
    Type for PASSING TIME.

    :ivar choice:
    :ivar alight_and_reboard: Whether can alight and reboard at stop.
    :ivar choice_1:
    """

    class Meta:
        name = "PassingTime_VersionedChildStructure"

    choice: Optional[
        Union[
            DatedVehicleJourneyRef,
            DatedSpecialServiceRef,
            SpecialServiceRef,
            TemplateServiceJourneyRef,
            ServiceJourneyRef,
            DeadRunRef,
            VehicleJourneyRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DatedVehicleJourneyRef",
                    "type": DatedVehicleJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedSpecialServiceRef",
                    "type": DatedSpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialServiceRef",
                    "type": SpecialServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
    alight_and_reboard: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AlightAndReboard",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice_1: Optional[
        Union[
            FarePointInPatternRef,
            StopPointInJourneyPatternRef,
            TimingPointInJourneyPatternRef,
            PointInJourneyPatternRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FarePointInPatternRef",
                    "type": FarePointInPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopPointInJourneyPatternRef",
                    "type": StopPointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimingPointInJourneyPatternRef",
                    "type": TimingPointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointInJourneyPatternRef",
                    "type": PointInJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
