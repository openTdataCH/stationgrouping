from dataclasses import dataclass, field
from typing import Optional

from generated.access_right_parameter_assignments_rel_structure import (
    AccessRightParameterAssignmentsRelStructure,
)
from generated.controllable_element_prices_rel_structure import (
    ControllableElementPricesRelStructure,
)
from generated.controllable_elements_in_sequence_rel_structure import (
    ControllableElementsInSequenceRelStructure,
)
from generated.priceable_object_version_structure import (
    PriceableObjectVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ControllableElementVersionStructure(PriceableObjectVersionStructure):
    """
    Type for CONTROLLABLE ELEMENT.

    :ivar access_right_parameter_assignments: ACCESS RIGHT PARAMETER
        ASSIGNMENTs associated with VALIDABLE ELEMENT.
    :ivar controllable_elements_in_sequence: VALIDITY PARAMETER
        ASSIGNMENTs associated with VALIDABLE. ELEMENT.
    :ivar prices: PRICEs for CONTROLLABLE ELEMENT.
    """

    class Meta:
        name = "ControllableElement_VersionStructure"

    access_right_parameter_assignments: Optional[
        AccessRightParameterAssignmentsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "accessRightParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    controllable_elements_in_sequence: Optional[
        ControllableElementsInSequenceRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "controllableElementsInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional[ControllableElementPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
