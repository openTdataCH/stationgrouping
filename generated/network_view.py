from dataclasses import dataclass

from generated.network_derived_view_structure import (
    NetworkDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkView(NetworkDerivedViewStructure):
    """
    Simplified view of a NETWORK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
