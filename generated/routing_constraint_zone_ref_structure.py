from dataclasses import dataclass

from generated.zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoutingConstraintZoneRefStructure(ZoneRefStructure):
    """
    Type for a reference to a ROUTING CONSTRAINT ZONE.
    """
