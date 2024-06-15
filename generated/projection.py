from dataclasses import dataclass

from generated.projection_version_structure import ProjectionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Projection(ProjectionVersionStructure):
    """An oriented correspondence - of the shape of an ENTITY on a source layer, - onto a ENTITY in a target layer: e.g. POINT, LINK, LINK SEQUENCE, COMPLEX FEATURE, - within a defined TYPE OF PROJECTION."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
