from dataclasses import dataclass

from generated.retail_device_version_structure import (
    RetailDeviceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailDevice(RetailDeviceVersionStructure):
    """A retail device used to sell fare products.

    Can be used to record fulfilment.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
