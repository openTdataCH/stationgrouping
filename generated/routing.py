from dataclasses import dataclass

from generated.routing_version_structure import RoutingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Routing(RoutingVersionStructure):
    """
    Limitations on routing of a fare.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
