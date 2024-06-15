from dataclasses import dataclass

from generated.route_link_ref_structure import RouteLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteLinkRef(RouteLinkRefStructure):
    """
    Reference to a ROUTE LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
