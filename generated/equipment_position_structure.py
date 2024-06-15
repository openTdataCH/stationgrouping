from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from generated.access_equipment_ref import AccessEquipmentRef
from generated.access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from generated.activated_equipment_ref import ActivatedEquipmentRef
from generated.assistance_booking_service_ref import (
    AssistanceBookingServiceRef,
)
from generated.assistance_service_ref import AssistanceServiceRef
from generated.catering_service_ref import CateringServiceRef
from generated.communication_service_ref import CommunicationServiceRef
from generated.complaints_service_ref import ComplaintsServiceRef
from generated.crossing_equipment_ref import CrossingEquipmentRef
from generated.customer_service_ref import CustomerServiceRef
from generated.cycle_storage_equipment_ref import CycleStorageEquipmentRef
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.entrance_equipment_ref import EntranceEquipmentRef
from generated.equipment_ref import EquipmentRef
from generated.escalator_equipment_ref import EscalatorEquipmentRef
from generated.general_sign_ref import GeneralSignRef
from generated.heading_sign_ref import HeadingSignRef
from generated.help_point_equipment_ref import HelpPointEquipmentRef
from generated.hire_service_ref import HireServiceRef
from generated.left_luggage_service_ref import LeftLuggageServiceRef
from generated.lift_equipment_ref import LiftEquipmentRef
from generated.local_service_ref import LocalServiceRef
from generated.location_structure_2 import LocationStructure2
from generated.lost_property_service_ref import LostPropertyServiceRef
from generated.luggage_locker_equipment_ref import LuggageLockerEquipmentRef
from generated.luggage_service_ref import LuggageServiceRef
from generated.meeting_point_service_ref import MeetingPointServiceRef
from generated.money_service_ref import MoneyServiceRef
from generated.multilingual_string import MultilingualString
from generated.passenger_equipment_ref import PassengerEquipmentRef
from generated.passenger_information_equipment_ref import (
    PassengerInformationEquipmentRef,
)
from generated.passenger_safety_equipment_ref import (
    PassengerSafetyEquipmentRef,
)
from generated.place_lighting_equipment_ref import PlaceLightingEquipmentRef
from generated.place_sign_ref import PlaceSignRef
from generated.point_ref_structure import PointRefStructure
from generated.queueing_equipment_ref import QueueingEquipmentRef
from generated.ramp_equipment_ref import RampEquipmentRef
from generated.retail_device_ref import RetailDeviceRef
from generated.retail_service_ref import RetailServiceRef
from generated.rough_surface_ref import RoughSurfaceRef
from generated.rubbish_disposal_equipment_ref import (
    RubbishDisposalEquipmentRef,
)
from generated.sanitary_equipment_ref import SanitaryEquipmentRef
from generated.seating_equipment_ref import SeatingEquipmentRef
from generated.shelter_equipment_ref import ShelterEquipmentRef
from generated.sign_equipment_ref import SignEquipmentRef
from generated.site_equipment_ref import SiteEquipmentRef
from generated.staircase_equipment_ref import StaircaseEquipmentRef
from generated.ticket_validator_equipment_ref import (
    TicketValidatorEquipmentRef,
)
from generated.ticketing_equipment_ref import TicketingEquipmentRef
from generated.ticketing_service_ref import TicketingServiceRef
from generated.travelator_equipment_ref import TravelatorEquipmentRef
from generated.trolley_stand_equipment_ref import TrolleyStandEquipmentRef
from generated.vehicle_charging_equipment_ref import (
    VehicleChargingEquipmentRef,
)
from generated.vehicle_equipment_ref import VehicleEquipmentRef
from generated.waiting_equipment_ref import WaitingEquipmentRef
from generated.waiting_room_equipment_ref import WaitingRoomEquipmentRef
from generated.wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EquipmentPositionStructure(DataManagedObjectStructure):
    """
    Type for EQUIPMENT POSITION.

    :ivar choice:
    :ivar description: Description of location of EQUIPMENT.
    :ivar location: Absolute location of EQUIPMENT.
    :ivar reference_point_ref: Location . If absent, use top left corner
        of containing space. If present should be an entrance or other
        specific point within the on the Space containing the EQUIPMENT.
    :ivar xoffset: Horizontal offset from reference point.
    :ivar yoffset: Vertical offset from reference point.
    """

    choice: Optional[
        Union[
            RetailDeviceRef,
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
            VehicleChargingEquipmentRef,
            CycleStorageEquipmentRef,
            TicketValidatorEquipmentRef,
            TicketingEquipmentRef,
            TrolleyStandEquipmentRef,
            SeatingEquipmentRef,
            ShelterEquipmentRef,
            LuggageLockerEquipmentRef,
            WaitingRoomEquipmentRef,
            WaitingEquipmentRef,
            SiteEquipmentRef,
            HeadingSignRef,
            GeneralSignRef,
            PlaceSignRef,
            SignEquipmentRef,
            PlaceLightingEquipmentRef,
            RoughSurfaceRef,
            StaircaseEquipmentRef,
            QueueingEquipmentRef,
            TravelatorEquipmentRef,
            EscalatorEquipmentRef,
            LiftEquipmentRef,
            CrossingEquipmentRef,
            RampEquipmentRef,
            EntranceEquipmentRef,
            AccessEquipmentRef,
            ActivatedEquipmentRef,
            PassengerInformationEquipmentRef,
            RubbishDisposalEquipmentRef,
            HelpPointEquipmentRef,
            PassengerSafetyEquipmentRef,
            SanitaryEquipmentRef,
            WheelchairVehicleRef,
            AccessVehicleEquipmentRef,
            VehicleEquipmentRef,
            PassengerEquipmentRef,
            EquipmentRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailDeviceRef",
                    "type": RetailDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                    "name": "VehicleChargingEquipmentRef",
                    "type": VehicleChargingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CycleStorageEquipmentRef",
                    "type": CycleStorageEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketValidatorEquipmentRef",
                    "type": TicketValidatorEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingEquipmentRef",
                    "type": TicketingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrolleyStandEquipmentRef",
                    "type": TrolleyStandEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeatingEquipmentRef",
                    "type": SeatingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ShelterEquipmentRef",
                    "type": ShelterEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageLockerEquipmentRef",
                    "type": LuggageLockerEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaitingRoomEquipmentRef",
                    "type": WaitingRoomEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaitingEquipmentRef",
                    "type": WaitingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteEquipmentRef",
                    "type": SiteEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadingSignRef",
                    "type": HeadingSignRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSignRef",
                    "type": GeneralSignRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceSignRef",
                    "type": PlaceSignRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SignEquipmentRef",
                    "type": SignEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceLightingEquipmentRef",
                    "type": PlaceLightingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoughSurfaceRef",
                    "type": RoughSurfaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StaircaseEquipmentRef",
                    "type": StaircaseEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QueueingEquipmentRef",
                    "type": QueueingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelatorEquipmentRef",
                    "type": TravelatorEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EscalatorEquipmentRef",
                    "type": EscalatorEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LiftEquipmentRef",
                    "type": LiftEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrossingEquipmentRef",
                    "type": CrossingEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RampEquipmentRef",
                    "type": RampEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceEquipmentRef",
                    "type": EntranceEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessEquipmentRef",
                    "type": AccessEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ActivatedEquipmentRef",
                    "type": ActivatedEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerInformationEquipmentRef",
                    "type": PassengerInformationEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RubbishDisposalEquipmentRef",
                    "type": RubbishDisposalEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HelpPointEquipmentRef",
                    "type": HelpPointEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSafetyEquipmentRef",
                    "type": PassengerSafetyEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SanitaryEquipmentRef",
                    "type": SanitaryEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WheelchairVehicleRef",
                    "type": WheelchairVehicleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessVehicleEquipmentRef",
                    "type": AccessVehicleEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEquipmentRef",
                    "type": VehicleEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerEquipmentRef",
                    "type": PassengerEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EquipmentRef",
                    "type": EquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    location: Optional[LocationStructure2] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    reference_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "ReferencePointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    xoffset: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "XOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    yoffset: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "YOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
