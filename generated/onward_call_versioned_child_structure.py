from dataclasses import dataclass, field
from typing import Optional

from generated.call_versioned_child_structure import (
    CallVersionedChildStructure,
)
from generated.estimated_passing_time_view import EstimatedPassingTimeView
from generated.target_passing_time_view import TargetPassingTimeView

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnwardCallVersionedChildStructure(CallVersionedChildStructure):
    """
    Data type for Onward  CALL.
    """

    class Meta:
        name = "OnwardCall_VersionedChildStructure"

    target_passing_time_view: Optional[TargetPassingTimeView] = field(
        default=None,
        metadata={
            "name": "TargetPassingTimeView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    estimated_passing_time_view: Optional[EstimatedPassingTimeView] = field(
        default=None,
        metadata={
            "name": "EstimatedPassingTimeView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
