from dataclasses import dataclass

from generated.group_of_distribution_channels_version_structure import (
    GroupOfDistributionChannelsVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfDistributionChannels(GroupOfDistributionChannelsVersionStructure):
    """A package to be sold as a whole, consisting of one or several FARE PRODUCTs
    materialised thanks to one or several TRAVEL DOCUMENTs.

    The FARE PRODUCTs may be either directly attached to the TRAVEL
    DOCUMENTs, or may be reloadable on the TRAVEL DOCUMENTs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
