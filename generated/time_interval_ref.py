from dataclasses import dataclass

from generated.time_interval_ref_structure import TimeIntervalRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TimeIntervalRef(TimeIntervalRefStructure):
    """
    Reference to a TIME INTERVAL.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
