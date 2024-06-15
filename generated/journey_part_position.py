from dataclasses import dataclass, field
from typing import Any

from generated.journey_part_position_versioned_child_structure import (
    JourneyPartPositionVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPartPosition(JourneyPartPositionVersionedChildStructure):
    """Position in train of JOURNEY PART from a given stop.

    +v1.1.

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
