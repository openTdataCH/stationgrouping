from dataclasses import dataclass, field
from typing import Any

from generated.notice_assignment_derived_view_structure import (
    NoticeAssignmentDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NoticeAssignmentView(NoticeAssignmentDerivedViewStructure):
    """View of a NOTICE ASSIGNMENT.

    for use in a specific context such as a CALL. This can be used to
    embed the notice itself in the context.

    :ivar name: Name of ASSIGNMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    name: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
