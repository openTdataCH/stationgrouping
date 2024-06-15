from dataclasses import dataclass

from generated.data_object_delivery_structure import (
    DataObjectDeliveryStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectDelivery(DataObjectDeliveryStructure):
    """
    Delivery for NeTEx   Service containing  one or more  NeTEx  Data Objects,.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
