from dataclasses import dataclass

from generated.suspending_version_structure import SuspendingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Suspending(SuspendingVersionStructure):
    """
    Conditions governing suspension of a FARE PRODUCT, e.g.  period pass or
    subscription.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
