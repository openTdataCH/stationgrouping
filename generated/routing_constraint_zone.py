from dataclasses import dataclass

from generated.routing_constraint_zone_version_structure import (
    RoutingConstraintZoneVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutingConstraintZone(RoutingConstraintZoneVersionStructure):
    """A constraint on the use of a service.

    The service, on this specific JOURNEY PATTERN (usually a FTS JOURNEY
    PATTERN) cannot operate when another (regular) service operates.
    This may occur only on subpart of the JOURNEY PATTERN, or only on
    one or some specific SCHEDULED STOP POINTs within the pattern.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
