from dataclasses import dataclass, field
from typing import Optional

from generated.version_of_object_ref_structure import (
    VersionOfObjectRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class EntityInVersionInFrameRefStructure(VersionOfObjectRefStructure):
    """
    Type for a VERSION FRAME MEMBER.
    """

    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
