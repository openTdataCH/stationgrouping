from dataclasses import dataclass

from generated.timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ScheduledStopPointRefStructure(TimingPointRefStructure):
    """
    Type for a reference to a SCHEDULED STOP POINT.
    """
