from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.dated_service_journey import DatedServiceJourney
from generated.dated_vehicle_journey import DatedVehicleJourney
from generated.dead_run import DeadRun
from generated.normal_dated_vehicle_journey import NormalDatedVehicleJourney
from generated.service_journey import ServiceJourney
from generated.special_service import SpecialService
from generated.template_service_journey import TemplateServiceJourney
from generated.vehicle_journey import VehicleJourney

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneysInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of  all JOURNEYs.
    """

    class Meta:
        name = "journeysInFrame_RelStructure"

    choice: List[
        Union[
            VehicleJourney,
            DatedVehicleJourney,
            NormalDatedVehicleJourney,
            ServiceJourney,
            DatedServiceJourney,
            DeadRun,
            SpecialService,
            TemplateServiceJourney,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehicleJourney",
                    "type": VehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedVehicleJourney",
                    "type": DatedVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NormalDatedVehicleJourney",
                    "type": NormalDatedVehicleJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourney",
                    "type": ServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DatedServiceJourney",
                    "type": DatedServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DeadRun",
                    "type": DeadRun,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SpecialService",
                    "type": SpecialService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TemplateServiceJourney",
                    "type": TemplateServiceJourney,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
