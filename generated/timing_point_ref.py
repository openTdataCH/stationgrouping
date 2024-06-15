from dataclasses import dataclass

from generated.timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimingPointRef(TimingPointRefStructure):
    """Reference to a TIMING POINT.

    If given by context does not need to be stated.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
