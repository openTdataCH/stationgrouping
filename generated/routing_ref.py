from dataclasses import dataclass

from generated.routing_ref_structure import RoutingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutingRef(RoutingRefStructure):
    """
    Reference to a ROUTING PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
