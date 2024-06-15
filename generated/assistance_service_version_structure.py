from dataclasses import dataclass, field
from typing import List, Optional

from generated.accessibility_tool_enumeration import (
    AccessibilityToolEnumeration,
)
from generated.assistance_availability_enumeration import (
    AssistanceAvailabilityEnumeration,
)
from generated.assistance_facility_list import AssistanceFacilityList
from generated.emergency_service_enumeration import EmergencyServiceEnumeration
from generated.local_service_version_structure import (
    LocalServiceVersionStructure,
)
from generated.safety_facility_enumeration import SafetyFacilityEnumeration
from generated.staffing_enumeration import StaffingEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssistanceServiceVersionStructure(LocalServiceVersionStructure):
    """
    Type for an ASSISTANCE SERVICE.

    :ivar assistance_facility_list:
    :ivar assistance_availability: Availability of assistance service.
    :ivar staffing: Staffing service.
    :ivar accessibility_tool_list:
    :ivar languages: Languages spoken for assistance.
    :ivar accessibility_trained_staff: Whether staff are accessibility
        trained.
    :ivar emergency_service_list: Emergency service assistance
        available.
    :ivar safety_facility_list: Safety facilities.
    """

    class Meta:
        name = "AssistanceService_VersionStructure"

    assistance_facility_list: Optional[AssistanceFacilityList] = field(
        default=None,
        metadata={
            "name": "AssistanceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    assistance_availability: Optional[AssistanceAvailabilityEnumeration] = (
        field(
            default=None,
            metadata={
                "name": "AssistanceAvailability",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    staffing: Optional[StaffingEnumeration] = field(
        default=None,
        metadata={
            "name": "Staffing",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_tool_list: List[AccessibilityToolEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityToolList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    languages: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Languages",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    accessibility_trained_staff: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AccessibilityTrainedStaff",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    emergency_service_list: List[EmergencyServiceEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "EmergencyServiceList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    safety_facility_list: List[SafetyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "SafetyFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
