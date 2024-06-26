from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.retail_device import RetailDevice
from generated.retail_device_ref import RetailDeviceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RetailDevicesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of RETAIL DEVICEs.
    """

    class Meta:
        name = "RetailDevices_RelStructure"

    retail_device_ref_or_retail_device: List[
        Union[RetailDeviceRef, RetailDevice]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailDeviceRef",
                    "type": RetailDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailDevice",
                    "type": RetailDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
