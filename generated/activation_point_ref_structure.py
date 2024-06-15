from dataclasses import dataclass

from generated.point_ref_structure import PointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationPointRefStructure(PointRefStructure):
    """
    Type for a reference to an ACTIVATION POINT.
    """
