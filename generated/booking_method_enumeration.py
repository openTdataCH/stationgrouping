from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class BookingMethodEnumeration(Enum):
    """
    Allowed values for Flexible Booking method.
    """

    CALL_DRIVER = "callDriver"
    CALL_OFFICE = "callOffice"
    ONLINE = "online"
    OTHER = "other"
    PHONE_AT_STOP = "phoneAtStop"
    TEXT = "text"
    NONE = "none"
