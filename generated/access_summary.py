from dataclasses import dataclass, field
from typing import Any

from generated.access_summary_versioned_child_structure import (
    AccessSummaryVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessSummary(AccessSummaryVersionedChildStructure):
    """
    Summary of a feature used in NAVIGATION PATH.

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
