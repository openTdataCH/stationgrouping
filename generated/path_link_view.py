from dataclasses import dataclass, field
from typing import Any

from generated.path_link_derived_view_structure import (
    PathLinkDerivedViewStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkView(PathLinkDerivedViewStructure):
    """
    A VIEW of a PATH LINK used to select items for presentation.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    branding_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
