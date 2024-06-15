from dataclasses import dataclass

from generated.group_of_lines_ref_structure import GroupOfLinesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfLinesRef(GroupOfLinesRefStructure):
    """
    Reference to a GROUP OF LINEs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
