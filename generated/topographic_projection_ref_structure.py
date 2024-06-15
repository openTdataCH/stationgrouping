from dataclasses import dataclass

from generated.zone_projection_ref_structure import ZoneProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicProjectionRefStructure(ZoneProjectionRefStructure):
    """
    Type for a reference to a TOPOGRAPHIC PROJECTION.
    """
