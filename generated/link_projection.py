from dataclasses import dataclass

from generated.link_projection_version_structure import (
    LinkProjectionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LinkProjection(LinkProjectionVersionStructure):
    """
    An oriented correspondence from one LINK of a source layer, onto an entity in a
    target layer: e.g. LINK SEQUENCE, COMPLEX FEATURE, within a defined TYPE OF
    PROJECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
