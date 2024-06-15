from dataclasses import dataclass

from generated.point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointRef(PointRefStructure):
    """
    Reference to a POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
