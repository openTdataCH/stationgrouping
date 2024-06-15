from dataclasses import dataclass

from generated.all_distribution_channels_ref_structure_element import (
    AllDistributionChannelsRefStructureElement,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllDistributionChannelsRef(AllDistributionChannelsRefStructureElement):
    """
    Reference to   All DISTRIBUTION CHANNELs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
