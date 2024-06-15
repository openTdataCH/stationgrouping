from dataclasses import dataclass, field
from typing import Optional

from generated.access_facility_list import AccessFacilityList
from generated.emergency_service_list import EmergencyServiceList
from generated.facility_set_version_structure import (
    FacilitySetVersionStructure,
)
from generated.hire_facility_list import HireFacilityList
from generated.luggage_locker_facility_list import LuggageLockerFacilityList
from generated.luggage_service_facility_list import LuggageServiceFacilityList
from generated.money_facility_list import MoneyFacilityList
from generated.parking_facility_list import ParkingFacilityList
from generated.staffing import Staffing

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SiteFacilitySetStructure(FacilitySetVersionStructure):
    """
    Type for a SITEFACILITY.

    :ivar access_facility_list: List of ACCESS FACILITies. + v1.1
    :ivar emergency_service_list: List of EMERGENCY SERVICE FACILITies.
    :ivar hire_facility_list: List of HIRE FACILITies.
    :ivar luggage_locker_facility_list: List of LUGGAGE LOCKER
        FACILITies.
    :ivar luggage_service_facility_list: List of LUGGAGE SERVICE
        FACILITies.
    :ivar money_facility_list: List of MONEY FACILITies.
    :ivar parking_facility_list: List of PARKING FACILITies.
    :ivar staffing: Classification of STAFFING.
    """

    access_facility_list: Optional[AccessFacilityList] = field(
        default=None,
        metadata={
            "name": "AccessFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    emergency_service_list: Optional[EmergencyServiceList] = field(
        default=None,
        metadata={
            "name": "EmergencyServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    hire_facility_list: Optional[HireFacilityList] = field(
        default=None,
        metadata={
            "name": "HireFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    luggage_locker_facility_list: Optional[LuggageLockerFacilityList] = field(
        default=None,
        metadata={
            "name": "LuggageLockerFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    luggage_service_facility_list: Optional[LuggageServiceFacilityList] = (
        field(
            default=None,
            metadata={
                "name": "LuggageServiceFacilityList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    money_facility_list: Optional[MoneyFacilityList] = field(
        default=None,
        metadata={
            "name": "MoneyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_facility_list: Optional[ParkingFacilityList] = field(
        default=None,
        metadata={
            "name": "ParkingFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    staffing: Optional[Staffing] = field(
        default=None,
        metadata={
            "name": "Staffing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
