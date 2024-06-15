from dataclasses import dataclass

from generated.group_of_operators_structure import GroupOfOperatorsStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfOperators(GroupOfOperatorsStructure):
    """
    A grouping of OPERATORs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
