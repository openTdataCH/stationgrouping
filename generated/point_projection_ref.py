from dataclasses import dataclass

from generated.point_projection_ref_structure import (
    PointProjectionRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointProjectionRef(PointProjectionRefStructure):
    """
    Reference to a PROJECTION.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
