from dataclasses import dataclass

from generated.routing_constraint_zone_ref_structure import (
    RoutingConstraintZoneRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutingConstraintZoneRef(RoutingConstraintZoneRefStructure):
    """
    Reference to a ROUTING CONSTRAINT ZONE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
