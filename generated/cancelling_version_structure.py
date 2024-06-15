from dataclasses import dataclass, field
from typing import Optional

from generated.booking_arrangements_structure import (
    BookingArrangementsStructure,
)
from generated.usage_parameter_version_structure import (
    UsageParameterVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CancellingVersionStructure(UsageParameterVersionStructure):
    """
    Type for CANCELLING.

    :ivar booking_arrangements: Booking Arrangements for Cancellations.
    """

    class Meta:
        name = "Cancelling_VersionStructure"

    booking_arrangements: Optional[BookingArrangementsStructure] = field(
        default=None,
        metadata={
            "name": "BookingArrangements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
