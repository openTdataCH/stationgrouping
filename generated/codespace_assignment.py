from dataclasses import dataclass, field
from typing import Any

from generated.codespace_assignment_versioned_child_structure import (
    CodespaceAssignmentVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CodespaceAssignment(CodespaceAssignmentVersionedChildStructure):
    """
    Assignment of use of a CODESPACE to identify data within a given ZONE.

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
