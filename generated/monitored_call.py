from dataclasses import dataclass

from generated.monitored_call_versioned_child_structure import (
    MonitoredCallVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MonitoredCall(MonitoredCallVersionedChildStructure):
    """
    Current monitored real-tieme CALL.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
