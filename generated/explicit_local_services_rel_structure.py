from dataclasses import dataclass, field
from typing import List, Union

from generated.assistance_booking_service import AssistanceBookingService
from generated.assistance_booking_service_ref import (
    AssistanceBookingServiceRef,
)
from generated.assistance_service import AssistanceService
from generated.assistance_service_ref import AssistanceServiceRef
from generated.catering_service import CateringService
from generated.catering_service_ref import CateringServiceRef
from generated.communication_service import CommunicationService
from generated.communication_service_ref import CommunicationServiceRef
from generated.complaints_service import ComplaintsService
from generated.complaints_service_ref import ComplaintsServiceRef
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.customer_service import CustomerService
from generated.customer_service_ref import CustomerServiceRef
from generated.hire_service import HireService
from generated.hire_service_ref import HireServiceRef
from generated.left_luggage_service import LeftLuggageService
from generated.left_luggage_service_ref import LeftLuggageServiceRef
from generated.local_service_ref import LocalServiceRef
from generated.lost_property_service import LostPropertyService
from generated.lost_property_service_ref import LostPropertyServiceRef
from generated.luggage_service import LuggageService
from generated.luggage_service_ref import LuggageServiceRef
from generated.meeting_point_service import MeetingPointService
from generated.meeting_point_service_ref import MeetingPointServiceRef
from generated.money_service import MoneyService
from generated.money_service_ref import MoneyServiceRef
from generated.retail_service import RetailService
from generated.retail_service_ref import RetailServiceRef
from generated.ticketing_service import TicketingService
from generated.ticketing_service_ref import TicketingServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ExplicitLocalServicesRelStructure(ContainmentAggregationStructure):
    """
    Items of LOCAL SERVICE EQUIPMENT that may be located in PLACEs within the SITE.
    """

    class Meta:
        name = "explicitLocalServices_RelStructure"

    choice: List[
        Union[
            AssistanceBookingServiceRef,
            CateringServiceRef,
            RetailServiceRef,
            MoneyServiceRef,
            HireServiceRef,
            CommunicationServiceRef,
            MeetingPointServiceRef,
            LeftLuggageServiceRef,
            LuggageServiceRef,
            LostPropertyServiceRef,
            ComplaintsServiceRef,
            CustomerServiceRef,
            AssistanceServiceRef,
            TicketingServiceRef,
            LocalServiceRef,
            AssistanceBookingService,
            CateringService,
            RetailService,
            MoneyService,
            HireService,
            CommunicationService,
            MeetingPointService,
            LostPropertyService,
            LeftLuggageService,
            ComplaintsService,
            CustomerService,
            LuggageService,
            AssistanceService,
            TicketingService,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AssistanceBookingServiceRef",
                    "type": AssistanceBookingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CateringServiceRef",
                    "type": CateringServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailServiceRef",
                    "type": RetailServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MoneyServiceRef",
                    "type": MoneyServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HireServiceRef",
                    "type": HireServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommunicationServiceRef",
                    "type": CommunicationServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingPointServiceRef",
                    "type": MeetingPointServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LeftLuggageServiceRef",
                    "type": LeftLuggageServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageServiceRef",
                    "type": LuggageServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LostPropertyServiceRef",
                    "type": LostPropertyServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplaintsServiceRef",
                    "type": ComplaintsServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerServiceRef",
                    "type": CustomerServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceServiceRef",
                    "type": AssistanceServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingServiceRef",
                    "type": TicketingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LocalServiceRef",
                    "type": LocalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceBookingService",
                    "type": AssistanceBookingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CateringService",
                    "type": CateringService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailService",
                    "type": RetailService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MoneyService",
                    "type": MoneyService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HireService",
                    "type": HireService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommunicationService",
                    "type": CommunicationService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MeetingPointService",
                    "type": MeetingPointService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LostPropertyService",
                    "type": LostPropertyService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LeftLuggageService",
                    "type": LeftLuggageService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ComplaintsService",
                    "type": ComplaintsService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerService",
                    "type": CustomerService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageService",
                    "type": LuggageService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AssistanceService",
                    "type": AssistanceService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingService",
                    "type": TicketingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
