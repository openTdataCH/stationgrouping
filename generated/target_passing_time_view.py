from dataclasses import dataclass

from generated.target_passing_time_view_structure import (
    TargetPassingTimeViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TargetPassingTimeView(TargetPassingTimeViewStructure):
    """
    Simplified TARGET PASSING TIME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
