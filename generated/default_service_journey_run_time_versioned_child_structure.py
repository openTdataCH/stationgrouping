from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration

from generated.journey_timing_versioned_child_structure import (
    JourneyTimingVersionedChildStructure,
)
from generated.service_journey_ref import ServiceJourneyRef
from generated.template_service_journey_ref import TemplateServiceJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DefaultServiceJourneyRunTimeVersionedChildStructure(
    JourneyTimingVersionedChildStructure
):
    """
    Type for DEFAULT SERVICE JOURNEY / RUN TIME.

    :ivar run_time: Run time as interval.
    :ivar template_service_journey_ref_or_service_journey_ref:
    """

    class Meta:
        name = "DefaultServiceJourneyRunTime_VersionedChildStructure"

    run_time: XmlDuration = field(
        metadata={
            "name": "RunTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    template_service_journey_ref_or_service_journey_ref: Optional[
        Union[TemplateServiceJourneyRef, ServiceJourneyRef]
    ] = field(
        default=None,
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
            ),
        },
    )
