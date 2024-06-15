from dataclasses import dataclass, field
from typing import List, Union

from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.service_journey_ref import ServiceJourneyRef
from generated.template_service_journey_ref import TemplateServiceJourneyRef
from generated.train_number_ref import TrainNumberRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelSpecificationJourneyRefsRelStructure(
    OneToManyRelationshipStructure
):
    """
    Type for a list of JOURNEYs.
    """

    class Meta:
        name = "travelSpecificationJourneyRefs_RelStructure"

    template_service_journey_ref_or_service_journey_ref_or_train_number_ref: List[
        Union[TemplateServiceJourneyRef, ServiceJourneyRef, TrainNumberRef]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
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
                    "name": "TrainNumberRef",
                    "type": TrainNumberRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
