from dataclasses import dataclass

from generated.turnaround_time_limit_time_ref_structure import (
    TurnaroundTimeLimitTimeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TurnaroundTimeLimitTimeRef(TurnaroundTimeLimitTimeRefStructure):
    """
    Reference to a TURNAROUND TIME LIMIT TIME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
