from dataclasses import dataclass, field
from typing import Any

from generated.entity_in_version_structure import (
    TimebandVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Timeband(TimebandVersionedChildStructure):
    """
    A period in a day, significant for some aspect of public transport, e.g.
    similar traffic conditions or fare category.

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
