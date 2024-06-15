from dataclasses import dataclass

from generated.stop_event_request_ref_structure import (
    StopEventRequestRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StopEventRequestRef(StopEventRequestRefStructure):
    """
    Reference to a STOP EVENT REQUEST.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
