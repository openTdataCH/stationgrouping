from dataclasses import dataclass

from generated.target_passing_time_versioned_child_structure import (
    TargetPassingTimeVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TargetPassingTime(TargetPassingTimeVersionedChildStructure):
    """
    TARGET PASSING TIME.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
