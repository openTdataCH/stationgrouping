from dataclasses import dataclass, field
from typing import Any

from generated.start_time_at_stop_point_versioned_child_structure import (
    StartTimeAtStopPointVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StartTimeAtStopPoint(StartTimeAtStopPointVersionedChildStructure):
    """
    A time at which a Fare demand  time band ( peak, off peak, etc  ) is deemed to
    begin  or end for trips at a particular SCHEDULED STOP POINT.

    :ivar validity_conditions_or_valid_between:
    :ivar alternative_texts: Additional Translations of text  elements.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    validity_conditions_or_valid_between: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    alternative_texts: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
