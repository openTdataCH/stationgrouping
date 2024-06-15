from dataclasses import dataclass, field
from typing import Optional

from generated.accessibility_info_facility_list import (
    AccessibilityInfoFacilityList,
)
from generated.accessibility_tool_list import AccessibilityToolList
from generated.assistance_facility_list import AssistanceFacilityList
from generated.car_service_facility_list import CarServiceFacilityList
from generated.catering_facility_list import CateringFacilityList
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.family_facility_list import FamilyFacilityList
from generated.fare_classes import FareClasses
from generated.gender_limitation import GenderLimitation
from generated.meal_facility_list import MealFacilityList
from generated.medical_facility_list import MedicalFacilityList
from generated.mobility_facility_list import MobilityFacilityList
from generated.multilingual_string import MultilingualString
from generated.nuisance_facility_list import NuisanceFacilityList
from generated.organisation_ref_structure import OrganisationRefStructure
from generated.passenger_comms_facility_list import PassengerCommsFacilityList
from generated.passenger_information_equipment_enumeration import (
    PassengerInformationEquipmentEnumeration,
)
from generated.passenger_information_facility_list import (
    PassengerInformationFacilityList,
)
from generated.retail_facility_list import RetailFacilityList
from generated.safety_facility_list import SafetyFacilityList
from generated.sanitary_facility_list import SanitaryFacilityList
from generated.ticketing_facility_list import TicketingFacilityList
from generated.ticketing_service_facility_list import (
    TicketingServiceFacilityList,
)
from generated.type_of_facility_ref import TypeOfFacilityRef
from generated.types_of_equipment_rel_structure import (
    TypesOfEquipmentRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FacilitySetVersionStructure(DataManagedObjectStructure):
    """
    Type for a FACILITY.

    :ivar provided_by_ref: Provider of FACILITY SET.
    :ivar description: Description of FACILITY SET.
    :ivar type_of_facility_ref:
    :ivar other_facilities: Arbitrary user defined Faciliy.
    :ivar accessibility_info_facility_list: List of ACCESSIBILITY
        INFORMATION FACILITies.
    :ivar assistance_facility_list: List of ASSISTANCE FACILITies.
    :ivar accessibility_tool_list: List of TYPEs of ACCESSIBILITY TOOLs.
    :ivar car_service_facility_list:
    :ivar catering_facility_list:
    :ivar family_facility_list:
    :ivar fare_classes: List of Fare Classes.
    :ivar gender_limitation:
    :ivar meal_facility_list:
    :ivar medical_facility_list:
    :ivar mobility_facility_list:
    :ivar nuisance_facility_list:
    :ivar passenger_comms_facility_list:
    :ivar passenger_information_equipment_list: List of PASSENGER
        INFORMATION Equipments.
    :ivar passenger_information_facility_list: List of PASSENGER
        INFORMATION FACILITies.
    :ivar retail_facility_list:
    :ivar safety_facility_list:
    :ivar sanitary_facility_list:
    :ivar ticketing_facility_list:
    :ivar ticketing_service_facility_list:
    """

    class Meta:
        name = "FacilitySet_VersionStructure"

    provided_by_ref: Optional[OrganisationRefStructure] = field(
        default=None,
        metadata={
            "name": "ProvidedByRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    type_of_facility_ref: Optional[TypeOfFacilityRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFacilityRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    other_facilities: Optional[TypesOfEquipmentRelStructure] = field(
        default=None,
        metadata={
            "name": "otherFacilities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_info_facility_list: Optional[
        AccessibilityInfoFacilityList
    ] = field(
        default=None,
        metadata={
            "name": "AccessibilityInfoFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    assistance_facility_list: Optional[AssistanceFacilityList] = field(
        default=None,
        metadata={
            "name": "AssistanceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_tool_list: Optional[AccessibilityToolList] = field(
        default=None,
        metadata={
            "name": "AccessibilityToolList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    car_service_facility_list: Optional[CarServiceFacilityList] = field(
        default=None,
        metadata={
            "name": "CarServiceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    catering_facility_list: Optional[CateringFacilityList] = field(
        default=None,
        metadata={
            "name": "CateringFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    family_facility_list: Optional[FamilyFacilityList] = field(
        default=None,
        metadata={
            "name": "FamilyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_classes: Optional[FareClasses] = field(
        default=None,
        metadata={
            "name": "FareClasses",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gender_limitation: Optional[GenderLimitation] = field(
        default=None,
        metadata={
            "name": "GenderLimitation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    meal_facility_list: Optional[MealFacilityList] = field(
        default=None,
        metadata={
            "name": "MealFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    medical_facility_list: Optional[MedicalFacilityList] = field(
        default=None,
        metadata={
            "name": "MedicalFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mobility_facility_list: Optional[MobilityFacilityList] = field(
        default=None,
        metadata={
            "name": "MobilityFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    nuisance_facility_list: Optional[NuisanceFacilityList] = field(
        default=None,
        metadata={
            "name": "NuisanceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_comms_facility_list: Optional[PassengerCommsFacilityList] = (
        field(
            default=None,
            metadata={
                "name": "PassengerCommsFacilityList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    passenger_information_equipment_list: Optional[
        PassengerInformationEquipmentEnumeration
    ] = field(
        default=None,
        metadata={
            "name": "PassengerInformationEquipmentList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passenger_information_facility_list: Optional[
        PassengerInformationFacilityList
    ] = field(
        default=None,
        metadata={
            "name": "PassengerInformationFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    retail_facility_list: Optional[RetailFacilityList] = field(
        default=None,
        metadata={
            "name": "RetailFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    safety_facility_list: Optional[SafetyFacilityList] = field(
        default=None,
        metadata={
            "name": "SafetyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sanitary_facility_list: Optional[SanitaryFacilityList] = field(
        default=None,
        metadata={
            "name": "SanitaryFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketing_facility_list: Optional[TicketingFacilityList] = field(
        default=None,
        metadata={
            "name": "TicketingFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketing_service_facility_list: Optional[TicketingServiceFacilityList] = (
        field(
            default=None,
            metadata={
                "name": "TicketingServiceFacilityList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
