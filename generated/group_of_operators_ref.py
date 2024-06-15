from dataclasses import dataclass

from generated.group_of_operators_ref_structure import (
    GroupOfOperatorsRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfOperatorsRef(GroupOfOperatorsRefStructure):
    """
    Reference to a GROUP OF OPERATORs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
