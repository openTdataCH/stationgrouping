from dataclasses import dataclass

from generated.zone_projection_version_structure import (
    ZoneProjectionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ZoneProjection(ZoneProjectionVersionStructure):
    """
    An oriented correspondence from one ZONE in a source layer,  onto a target
    entity : e.g.  POINT, COMPLEX FEATURE, within a defined TYPE OF PROJECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
