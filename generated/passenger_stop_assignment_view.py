from dataclasses import dataclass, field
from typing import Any

from generated.passenger_stop_assignment_derived_view_structure import (
    PassengerStopAssignmentDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerStopAssignmentView(PassengerStopAssignmentDerivedViewStructure):
    """View of an assignment of a SCHEDULED STOP POINT to a STOP PLACE and quay.

    etc.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    label: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    branding_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
