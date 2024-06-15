from dataclasses import dataclass

from generated.path_link_ref_by_value_structure import (
    PathLinkRefByValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkRefByValue(PathLinkRefByValueStructure):
    """
    Reference to a PATH LINK BY VALUE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
