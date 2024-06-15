from dataclasses import dataclass, field
from typing import Optional

from generated.accommodation_facility import AccommodationFacility
from generated.berth_facility import BerthFacility
from generated.class_of_use_ref import ClassOfUseRef
from generated.couchette_facility import CouchetteFacility
from generated.entity_in_version_structure import VersionedChildStructure
from generated.fare_class import FareClass
from generated.gender_limitation import GenderLimitation
from generated.multilingual_string import MultilingualString
from generated.nuisance_facility_list import NuisanceFacilityList
from generated.passenger_comms_facility_list import PassengerCommsFacilityList
from generated.sanitary_facility_enumeration import SanitaryFacilityEnumeration
from generated.service_facility_set_ref import ServiceFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccommodationVersionedChildStructure(VersionedChildStructure):
    """
    Type for allowed combinations of ACCOMMODATION.

    :ivar name: Name of Accomodation _v1.1
    :ivar service_facility_set_ref:
    :ivar fare_class: Fare class of ACCOMMODATION.
    :ivar class_of_use_ref:
    :ivar accommodation_facility: Type of ACCOMMODATION. . Default is
        seating.
    :ivar couchette_facility: Type of Couchette.
    :ivar maximum_number_of_berths:
    :ivar berth_facility: Classification of BERTH FACILITY.
    :ivar shower_facility:
    :ivar toilet_facility: Toilet facilities for ACCOMMODATION.
    :ivar gender_limitation:
    :ivar nuisance_facility_list:
    :ivar passenger_comms_facility_list:
    """

    class Meta:
        name = "Accommodation_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_facility_set_ref: Optional[ServiceFacilitySetRef] = field(
        default=None,
        metadata={
            "name": "ServiceFacilitySetRef",
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
    accommodation_facility: Optional[AccommodationFacility] = field(
        default=None,
        metadata={
            "name": "AccommodationFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    couchette_facility: Optional[CouchetteFacility] = field(
        default=None,
        metadata={
            "name": "CouchetteFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_number_of_berths: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfBerths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    berth_facility: Optional[BerthFacility] = field(
        default=None,
        metadata={
            "name": "BerthFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    shower_facility: Optional[SanitaryFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "ShowerFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    toilet_facility: Optional[SanitaryFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "ToiletFacility",
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
