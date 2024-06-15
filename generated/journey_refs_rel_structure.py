from dataclasses import dataclass, field
from typing import List, Union

from generated.dated_special_service_ref import DatedSpecialServiceRef
from generated.dated_vehicle_journey_ref import DatedVehicleJourneyRef
from generated.dead_run_ref import DeadRunRef
from generated.journey_designator import JourneyDesignator
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.service_designator import ServiceDesignator
from generated.service_journey_ref import ServiceJourneyRef
from generated.special_service_ref import SpecialServiceRef
from generated.template_service_journey_ref import TemplateServiceJourneyRef
from generated.vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of JOURNEYs.
    """

    class Meta:
        name = "journeyRefs_RelStructure"

    choice: List[
        Union[
            DatedVehicleJourneyRef,
            DatedSpecialServiceRef,
            SpecialServiceRef,
            TemplateServiceJourneyRef,
            ServiceJourneyRef,
            DeadRunRef,
            VehicleJourneyRef,
            JourneyDesignator,
            ServiceDesignator,
        ]
    ] = field(
        default_factory=list,
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
                {
                    "name": "JourneyDesignator",
                    "type": JourneyDesignator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceDesignator",
                    "type": ServiceDesignator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
