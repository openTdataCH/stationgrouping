from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime, XmlDuration

from generated.class_of_use_ref import ClassOfUseRef
from generated.companion_profile_ref import CompanionProfileRef
from generated.fare_class import FareClass
from generated.group_of_operators_ref import GroupOfOperatorsRef
from generated.group_ticket_ref import GroupTicketRef
from generated.operator_ref import OperatorRef
from generated.passenger_seat_ref import PassengerSeatRef
from generated.series_constraint_refs_rel_structure import (
    SeriesConstraintRefsRelStructure,
)
from generated.service_facility_set import ServiceFacilitySet
from generated.train_component_label_assignment_ref import (
    TrainComponentLabelAssignmentRef,
)
from generated.train_element_ref import TrainElementRef
from generated.travel_specification_journey_refs_rel_structure import (
    TravelSpecificationJourneyRefsRelStructure,
)
from generated.travel_specification_summary_endpoint_structure import (
    TravelSpecificationSummaryEndpointStructure,
)
from generated.type_of_fare_product_ref import TypeOfFareProductRef
from generated.type_of_product_category_ref import TypeOfProductCategoryRef
from generated.user_profile_ref import UserProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelSpecificationSummaryViewStructure:
    """Summary of key aspects of TRAVEL SPECIFICATION.

    +V1.1. This data should all be derivable from the detailed
    specification. v+1.1

    :ivar origin: Origin of Travel.  Note that for a point-to-point
        TARIFF the origin is assigned with a DISTANCE MATRIX ELEMENT.
    :ivar destination: Destination of Travel. Note that for a point-to-
        point TARIFF the origin is assigned with a DISTANCE MATRIX
        ELEMENT.
    :ivar start: Start tiem for trip or pass.
    :ivar end: End time for trip or pass.
    :ivar duration: DUration for trip or pass
    :ivar journeys: Specified journeys for trip.
    :ivar series_constraints: Routig for trip
    :ivar operator_ref_or_group_of_operators_ref:
    :ivar type_of_product_category_ref:
    :ivar type_of_fare_product_ref:
    :ivar fare_class:
    :ivar class_of_use_ref:
    :ivar companion_profile_ref_or_user_profile_ref:
    :ivar group_ticket_ref:
    :ivar maximum_number_of_users: Maimum number of users on a GROUP
        TICKET.
    :ivar train_element_ref:
    :ivar train_component_label_assignment_ref:
    :ivar passenger_seat_ref:
    :ivar service_facility_set:
    """

    origin: Optional[TravelSpecificationSummaryEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    destination: Optional[TravelSpecificationSummaryEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journeys: Optional[TravelSpecificationJourneyRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    series_constraints: Optional[SeriesConstraintRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "seriesConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operator_ref_or_group_of_operators_ref: Optional[
        Union[OperatorRef, GroupOfOperatorsRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
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
    type_of_fare_product_ref: Optional[TypeOfFareProductRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_class: Optional[FareClass] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_use_ref: Optional[ClassOfUseRef] = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    companion_profile_ref_or_user_profile_ref: Optional[
        Union[CompanionProfileRef, UserProfileRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompanionProfileRef",
                    "type": CompanionProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileRef",
                    "type": UserProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    group_ticket_ref: Optional[GroupTicketRef] = field(
        default=None,
        metadata={
            "name": "GroupTicketRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_of_users: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfUsers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_element_ref: Optional[TrainElementRef] = field(
        default=None,
        metadata={
            "name": "TrainElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_component_label_assignment_ref: Optional[
        TrainComponentLabelAssignmentRef
    ] = field(
        default=None,
        metadata={
            "name": "TrainComponentLabelAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_seat_ref: Optional[PassengerSeatRef] = field(
        default=None,
        metadata={
            "name": "PassengerSeatRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_facility_set: Optional[ServiceFacilitySet] = field(
        default=None,
        metadata={
            "name": "ServiceFacilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
