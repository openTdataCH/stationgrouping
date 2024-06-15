from dataclasses import dataclass

from generated.group_of_lines_version_structure import (
    GroupOfLinesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLines(GroupOfLinesVersionStructure):
    """
    A grouping of LINEs which will be commonly referenced for a specific purpose.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
