from dataclasses import dataclass, field
from typing import Any

from generated.alternative_quay_descriptor_versioned_child_structure import (
    AlternativeQuayDescriptorVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AlternativeQuayDescriptor(
    AlternativeQuayDescriptorVersionedChildStructure
):
    """
    An element of a STOP PLACE describing part of its structure.

    :ivar name_type: Type of Name - fixed value. Default is Alias.
    :ivar validity_conditions_or_valid_between:
    :ivar alternative_texts: Additional Translations of text  elements.
    :ivar type_of_name: Type of Name.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name_type: Any = field(
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
    type_of_name: str = field(
        metadata={
            "name": "TypeOfName",
            "type": "Element",
            "required": True,
        }
    )
