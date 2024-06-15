from dataclasses import dataclass

from generated.target_passing_time_ref_structure import (
    TargetPassingTimeRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TargetPassingTimeRef(TargetPassingTimeRefStructure):
    """
    Reference to a TARGET PASSING TIME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
