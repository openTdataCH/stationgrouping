from dataclasses import dataclass

from generated.relief_point_ref_structure import ReliefPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefPointRef(ReliefPointRefStructure):
    """
    Reference to a RELIEF POINT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
