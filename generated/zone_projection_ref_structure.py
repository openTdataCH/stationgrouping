from dataclasses import dataclass

from generated.projection_ref_structure import ProjectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ZoneProjectionRefStructure(ProjectionRefStructure):
    """
    Type for a reference to a ZONE PROJECTION.
    """
