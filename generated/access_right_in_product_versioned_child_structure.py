from dataclasses import dataclass, field
from typing import Optional, Union

from generated.fare_element_in_sequence_versioned_child_structure import (
    FareElementInSequenceVersionedChildStructure,
)
from generated.preassigned_fare_product_ref import PreassignedFareProductRef
from generated.supplement_product_ref import SupplementProductRef
from generated.validable_element_ref import ValidableElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessRightInProductVersionedChildStructure(
    FareElementInSequenceVersionedChildStructure
):
    """
    Type for ACCESS RIGHT IN PRODUCT.
    """

    class Meta:
        name = "AccessRightInProduct_VersionedChildStructure"

    validable_element_ref: Optional[ValidableElementRef] = field(
        default=None,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    supplement_product_ref_or_preassigned_fare_product_ref: Optional[
        Union[SupplementProductRef, PreassignedFareProductRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplementProductRef",
                    "type": SupplementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProductRef",
                    "type": PreassignedFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
