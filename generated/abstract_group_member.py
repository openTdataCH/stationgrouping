from dataclasses import dataclass, field
from typing import Any

from generated.abstract_group_member_versioned_child_structure import (
    AbstractGroupMemberVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AbstractGroupMember(AbstractGroupMemberVersionedChildStructure):
    """
    Abstract member of a GROUP OF ENTITY MEMBERs.

    :ivar description:
    :ivar validity_conditions_or_valid_between:
    :ivar alternative_texts: Additional Translations of text  elements.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    description: Any = field(
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
