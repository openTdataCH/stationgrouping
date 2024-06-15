from dataclasses import dataclass

from generated.distribution_channel_version_structure import (
    DistributionChannelVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistributionChannel(DistributionChannelVersionStructure):
    """
    A type of outlet for selling a product.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
