from dataclasses import dataclass, field
from typing import Any

from generated.fare_structure_element_price_versioned_child_structure import (
    FareStructureElementPriceVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareStructureElementPrice(
    FareStructureElementPriceVersionedChildStructure
):
    """A set of all possible price features of a FARE STRUCTURE ELEMENT: default total price, discount in value or percentage etc.

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
