from dataclasses import dataclass, field
from typing import Optional

from generated.distribution_channel_refs_rel_structure import (
    DistributionChannelRefsRelStructure,
)
from generated.group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfDistributionChannelsVersionStructure(
    GroupOfEntitiesVersionStructure
):
    """
    Type for GROUP OF DISTRIBUTION CHANNELs.

    :ivar members: DISTRIBUTION CHANNELs in Group.
    """

    class Meta:
        name = "GroupOfDistributionChannels_VersionStructure"

    members: Optional[DistributionChannelRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
