from dataclasses import dataclass

from generated.line_network_ref_structure import LineNetworkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineNetworkRef(LineNetworkRefStructure):
    """
    Reference to a LINE NETWORK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
