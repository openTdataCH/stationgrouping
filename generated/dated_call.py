from dataclasses import dataclass

from generated.dated_call_versioned_child_structure import (
    DatedCallVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DatedCall(DatedCallVersionedChildStructure):
    """A visit to a SCHEDULED STOP POINT as part of a VEHICLE JOURNEY.

    A CALL is a view of a POINT IN JOURNEY PATTERN that adds in derived
    data.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
