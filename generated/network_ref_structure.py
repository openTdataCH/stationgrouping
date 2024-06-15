from dataclasses import dataclass

from generated.group_of_lines_ref_structure import GroupOfLinesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkRefStructure(GroupOfLinesRefStructure):
    """
    Type for a reference to a NETWORK.
    """
