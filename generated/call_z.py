from dataclasses import dataclass

from generated.call_versioned_child_structure import (
    CallVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CallZ(CallVersionedChildStructure):
    """A visit to a SCHEDULED STOP POINT as part of a VEHICLE JOURNEY.

    A CALL is a view of a POINT IN JOURNEY PATTERN that adds in derived
    data. No Constraints
    """

    class Meta:
        name = "Call-Z"
        namespace = "http://www.netex.org.uk/netex"
