from dataclasses import dataclass, field
from typing import Any

from generated.estimated_passing_time_versioned_child_structure import (
    EstimatedPassingTimeVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EstimatedPassingTime(EstimatedPassingTimeVersionedChildStructure):
    """
    Estimated PASSING TIME.

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
