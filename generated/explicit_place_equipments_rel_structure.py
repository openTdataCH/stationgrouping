from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.crossing_equipment import CrossingEquipment
from generated.entrance_equipment import EntranceEquipment
from generated.escalator_equipment import EscalatorEquipment
from generated.general_sign_structure import GeneralSignStructure
from generated.heading_sign_structure import HeadingSignStructure
from generated.help_point_equipment import HelpPointEquipment
from generated.lift_equipment import LiftEquipment
from generated.other_place_equipment import OtherPlaceEquipment
from generated.passenger_safety_equipment import PassengerSafetyEquipment
from generated.place_lighting import PlaceLighting
from generated.place_sign_structure import PlaceSignStructure
from generated.queueing_equipment import QueueingEquipment
from generated.ramp_equipment import RampEquipment
from generated.rough_surface import RoughSurface
from generated.rubbish_disposal_equipment import RubbishDisposalEquipment
from generated.sanitary_equipment import SanitaryEquipment
from generated.staircase_equipment import StaircaseEquipment
from generated.ticket_validator_equipment import TicketValidatorEquipment
from generated.ticketing_equipment import TicketingEquipment
from generated.travelator_equipment import TravelatorEquipment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ExplicitPlaceEquipmentsRelStructure(ContainmentAggregationStructure):
    """
    Items of fixed EQUIPMENT that may be located in places within the STOP PLACE.
    """

    class Meta:
        name = "explicitPlaceEquipments_RelStructure"

    choice: List[
        Union[
            OtherPlaceEquipment,
            RoughSurface,
            EntranceEquipment,
            StaircaseEquipment,
            LiftEquipment,
            EscalatorEquipment,
            TravelatorEquipment,
            RampEquipment,
            QueueingEquipment,
            CrossingEquipment,
            PlaceLighting,
            PlaceSignStructure,
            HeadingSignStructure,
            GeneralSignStructure,
            HelpPointEquipment,
            PassengerSafetyEquipment,
            RubbishDisposalEquipment,
            SanitaryEquipment,
            TicketingEquipment,
            TicketValidatorEquipment,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OtherPlaceEquipment",
                    "type": OtherPlaceEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoughSurface",
                    "type": RoughSurface,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntranceEquipment",
                    "type": EntranceEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StaircaseEquipment",
                    "type": StaircaseEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LiftEquipment",
                    "type": LiftEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EscalatorEquipment",
                    "type": EscalatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelatorEquipment",
                    "type": TravelatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RampEquipment",
                    "type": RampEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QueueingEquipment",
                    "type": QueueingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CrossingEquipment",
                    "type": CrossingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceLighting",
                    "type": PlaceLighting,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PlaceSign",
                    "type": PlaceSignStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HeadingSign",
                    "type": HeadingSignStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralSign",
                    "type": GeneralSignStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HelpPointEquipment",
                    "type": HelpPointEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSafetyEquipment",
                    "type": PassengerSafetyEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RubbishDisposalEquipment",
                    "type": RubbishDisposalEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SanitaryEquipment",
                    "type": SanitaryEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketingEquipment",
                    "type": TicketingEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TicketValidatorEquipment",
                    "type": TicketValidatorEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
