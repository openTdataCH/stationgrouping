from dataclasses import dataclass

from generated.rough_surface_ref_structure import RoughSurfaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoughSurfaceRef(RoughSurfaceRefStructure):
    """
    Identifier of an ROUGH SURFACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
