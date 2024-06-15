from dataclasses import dataclass

from generated.group_of_timebands_versioned_child_structure import (
    GroupOfTimebandsVersionedChildStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfTimebands(GroupOfTimebandsVersionedChildStructure):
    """
    A period in a day, significant for some aspect of public transport, e.g.
    similar traffic conditions or fare category.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
