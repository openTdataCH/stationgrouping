from dataclasses import dataclass, field
from typing import List, Union

from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.type_of_retail_device import TypeOfRetailDevice
from generated.type_of_retail_device_ref import TypeOfRetailDeviceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypesOfRetailDeviceRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of TYPE OF RETAIL DEVICEs.
    """

    class Meta:
        name = "typesOfRetailDevice_RelStructure"

    type_of_retail_device_ref_or_type_of_retail_device: List[
        Union[TypeOfRetailDeviceRef, TypeOfRetailDevice]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfRetailDeviceRef",
                    "type": TypeOfRetailDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfRetailDevice",
                    "type": TypeOfRetailDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
