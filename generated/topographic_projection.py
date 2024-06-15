from dataclasses import dataclass

from generated.topographic_projection_version_structure import (
    TopographicProjectionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicProjection(TopographicProjectionVersionStructure):
    """An correspondence from a ZONE in a source layer,  onto a name place: i.e.
    TOPOGRAPHIC PLACE.

    +v1.1
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
