from dataclasses import dataclass, field
from typing import Any

from generated.type_of_link_sequence_value_structure import (
    TypeOfLinkSequenceValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfLinkSequence(TypeOfLinkSequenceValueStructure):
    """
    A classification of LINK SEQUENCEs according to their functional purpose.

    :ivar validity_conditions_or_valid_between:
    :ivar alternative_texts: Additional Translations of text  elements.
    :ivar name_of_classified_entity_class: Name of Class of the ENTITY.
        Allows reflection. Fixed for each ENTITY type.
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
    name_of_classified_entity_class: str = field(
        init=False,
        default="LinkSequence",
        metadata={
            "name": "nameOfClassifiedEntityClass",
            "type": "Attribute",
        },
    )
