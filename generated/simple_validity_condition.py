from dataclasses import dataclass, field
from typing import Any

from generated.entity_in_version_structure import ValidBetweenVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SimpleValidityCondition(ValidBetweenVersionStructure):
    """OPTIMISATION Simple version of a VALIDITY CONDITION used in order to
    characterise a given VERSION of a VERSION FRAME.

    Comprises a simple period.Deprecated.

    :ivar name: Name of VALIDITY CONDITION.
    :ivar description: Description of VALIDITY CONDITION.
    :ivar conditioned_object_ref: Entity to which condition specifically
        attaches.
    :ivar with_condition_ref: CONDITION with which this rule is
        logically ANDed.
    :ivar key_list: A list of alternative Key values for an element.
    :ivar extensions:
    :ivar branding_ref:
    :ivar validity_conditions_or_valid_between:
    :ivar alternative_texts: Additional Translations of text  elements.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    description: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    conditioned_object_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    with_condition_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    key_list: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    extensions: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    branding_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
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
