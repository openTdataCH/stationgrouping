from dataclasses import dataclass

from generated.network_ref_structure import NetworkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkRef(NetworkRefStructure):
    """
    Reference to a NETWORK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
