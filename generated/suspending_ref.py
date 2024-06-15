from dataclasses import dataclass

from generated.suspending_ref_structure import SuspendingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SuspendingRef(SuspendingRefStructure):
    """
    Reference to a SUSPENDING.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
