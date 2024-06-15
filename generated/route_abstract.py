from dataclasses import dataclass

from generated.sections_in_sequence_rel_structure import (
    LinkSequenceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteAbstract(LinkSequenceVersionStructure):
    """
    Dummy supertype for Route.
    """

    class Meta:
        name = "Route_"
        namespace = "http://www.netex.org.uk/netex"
