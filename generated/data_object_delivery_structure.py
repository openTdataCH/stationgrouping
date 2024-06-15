from dataclasses import dataclass, field
from typing import Optional

from generated.abstract_service_delivery_structure import (
    AbstractServiceDeliveryStructure,
)
from generated.data_object_request import DataObjectRequest
from generated.data_objects_rel_structure import DataObjectsRelStructure
from generated.extensions_2 import Extensions2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectDeliveryStructure(AbstractServiceDeliveryStructure):
    """
    Data type for Delivery for  Service containing  one or more  NeTEx  Data
    Objects,.

    :ivar data_object_request:
    :ivar data_objects: NeTEx Entities of any type.
    :ivar extensions:
    """

    data_object_request: Optional[DataObjectRequest] = field(
        default=None,
        metadata={
            "name": "DataObjectRequest",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    data_objects: Optional[DataObjectsRelStructure] = field(
        default=None,
        metadata={
            "name": "dataObjects",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    extensions: Optional[Extensions2] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
