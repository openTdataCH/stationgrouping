from dataclasses import dataclass

from generated.rough_surface_structure import RoughSurfaceStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoughSurface(RoughSurfaceStructure):
    """
    Specialisation of PLACE EQUIPMENT for rough surfaces, giving properties of
    surface texture, mainly for impaired person information.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
