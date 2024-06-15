from dataclasses import dataclass

from generated.line_network_version_structure import (
    LineNetworkVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LineNetwork(LineNetworkVersionStructure):
    """A description of the topological connectivity of a LINE as a set of LINE
    SECTIONs.

    This is sufficient to draw a route map for the whole line including
    branches and loops.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
