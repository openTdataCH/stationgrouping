from dataclasses import dataclass

from generated.previous_call_versioned_child_structure import (
    PreviousCallVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PreviousCall(PreviousCallVersionedChildStructure):
    """
    An already completed CALL of  a VEHICLE JOURNEY that occurred earlier in the
    the JOURNEY PATTERN before the current stop.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
