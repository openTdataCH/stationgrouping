from dataclasses import dataclass

from generated.timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class BorderPointRefStructure(TimingPointRefStructure):
    """
    Type for a reference to a BORDER POINT.
    """
