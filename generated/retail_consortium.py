from dataclasses import dataclass

from generated.retail_consortium_version_structure import (
    RetailConsortiumVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailConsortium(RetailConsortiumVersionStructure):
    """
    A group of ORGANISATIONs formally incorporated as a retailer of fare products.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
