from dataclasses import dataclass, field
from typing import Optional, Union

from generated.accessibility_assessment import AccessibilityAssessment
from generated.all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from generated.external_object_ref_structure import ExternalObjectRefStructure
from generated.journey_accountings_rel_structure import (
    JourneyAccountingsRelStructure,
)
from generated.link_sequence_projection import LinkSequenceProjection
from generated.link_sequence_projection_ref import LinkSequenceProjectionRef
from generated.notice_assignments_rel_structure import (
    NoticeAssignmentsRelStructure,
)
from generated.sections_in_sequence_rel_structure import (
    LinkSequenceVersionStructure,
)
from generated.transport_submode import TransportSubmode
from generated.type_of_product_category_ref import TypeOfProductCategoryRef
from generated.type_of_service_ref import TypeOfServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyVersionStructure(LinkSequenceVersionStructure):
    """
    Type for JOURNEY.

    :ivar transport_mode: Mode of transport of JOURNEY.
    :ivar transport_submode:
    :ivar external_vehicle_journey_ref: An alternative  code that
        uniquely identifies the JOURNEY. Specifically for use in AVMS
        systems. For VDV compatibility.
    :ivar type_of_product_category_ref:
    :ivar type_of_service_ref:
    :ivar link_sequence_projection_ref_or_link_sequence_projection:
    :ivar monitored: Whether the journey will be monitored in real time.
    :ivar accessibility_assessment:
    :ivar journey_accountings: JOURNEY ACCOUNTING to be used to
        attribute JOURNEY costs.
    :ivar notice_assignments: NOTICEs  relevant for the whole GROUP OF
        SERVICEs.
    """

    class Meta:
        name = "Journey_VersionStructure"

    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_submode: Optional[TransportSubmode] = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    external_vehicle_journey_ref: Optional[ExternalObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "ExternalVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_product_category_ref: Optional[TypeOfProductCategoryRef] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_service_ref: Optional[TypeOfServiceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    link_sequence_projection_ref_or_link_sequence_projection: Optional[
        Union[LinkSequenceProjectionRef, LinkSequenceProjection]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LinkSequenceProjectionRef",
                    "type": LinkSequenceProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LinkSequenceProjection",
                    "type": LinkSequenceProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_accountings: Optional[JourneyAccountingsRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyAccountings",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
