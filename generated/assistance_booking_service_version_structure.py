from dataclasses import dataclass, field
from typing import Optional, Union

from generated.assistance_availability_enumeration import (
    AssistanceAvailabilityEnumeration,
)
from generated.authority_ref import AuthorityRef
from generated.booking_arrangements_structure import (
    BookingArrangementsStructure,
)
from generated.contact_structure import ContactStructure
from generated.flexible_line_ref import FlexibleLineRef
from generated.line_ref import LineRef
from generated.local_service_version_structure import (
    LocalServiceVersionStructure,
)
from generated.notice_assignments_rel_structure import (
    NoticeAssignmentsRelStructure,
)
from generated.operator_ref import OperatorRef
from generated.vehicle_mode import VehicleMode
from generated.version_of_object_ref_structure import (
    VersionOfObjectRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssistanceBookingServiceVersionStructure(LocalServiceVersionStructure):
    """
    Type for ASSISTANCE BOOKING SERVICE.

    :ivar assistance_availability: Availilability of assistance.
    :ivar wheelchair_booking_required: Whether a booking is needed to
        use a wheelchair.
    :ivar booking_contact: Contact details for ASSISTANCE BOOKING
        SERVICE.
    :ivar booking_arrangements: Booking conditions for ASSISTANCE
        BOOKING SERVICE.
    :ivar vehicle_mode:
    :ivar authority_ref_or_operator_ref:
    :ivar flexible_line_ref_or_line_ref:
    :ivar booked_object_ref: Specific object to which booking relates,
        e.g. SCHEDULED STOP POINT, STOP, VEHICLE JOURNEY, etc.
    :ivar notice_assignments: NOTICEs for ASSISTANCE BOOKING SERVICE.
    """

    class Meta:
        name = "AssistanceBookingService_VersionStructure"

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
    wheelchair_booking_required: Optional[bool] = field(
        default=None,
        metadata={
            "name": "WheelchairBookingRequired",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_contact: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "BookingContact",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    booking_arrangements: Optional[BookingArrangementsStructure] = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_mode: Optional[VehicleMode] = field(
        default=None,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    authority_ref_or_operator_ref: Optional[
        Union[AuthorityRef, OperatorRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    flexible_line_ref_or_line_ref: Optional[
        Union[FlexibleLineRef, LineRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    booked_object_ref: Optional[VersionOfObjectRefStructure] = field(
        default=None,
        metadata={
            "name": "BookedObjectRef",
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
