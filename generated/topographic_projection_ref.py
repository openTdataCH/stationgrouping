from dataclasses import dataclass

from generated.topographic_projection_ref_structure import (
    TopographicProjectionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TopographicProjectionRef(TopographicProjectionRefStructure):
    """
    Reference to a TOPOGRAPHIC PROJECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
