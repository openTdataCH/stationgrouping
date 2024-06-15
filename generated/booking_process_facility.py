from dataclasses import dataclass, field

from generated.booking_process_enumeration import BookingProcessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BookingProcessFacility:
    """Classification of BOOKING PROCESS FACILITY type - UIC 7037 Code list."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: BookingProcessEnumeration = field(
        metadata={
            "required": True,
        }
    )
