from dataclasses import dataclass, field
from typing import Optional

from generated.activated_equipment_ref_structure import (
    ActivatedEquipmentRefStructure,
)
from generated.activation_link_ref_structure import ActivationLinkRefStructure
from generated.activation_point_ref_structure import (
    ActivationPointRefStructure,
)
from generated.assignment_version_structure_1 import (
    AssignmentVersionStructure1,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationAssignmentVersionStructure(AssignmentVersionStructure1):
    """
    Type for an ACTIVATION ASSIGNMENT.

    :ivar equipment_ref: ACTIVATED EQUIPMENT for which this is the
        assignment - may be omitted if given by context.
    :ivar link_ref: ACTIVATION LINK for assignment.
    :ivar point_ref: ACTIVATION POINT for assignment.
    """

    class Meta:
        name = "ActivationAssignment_VersionStructure"

    equipment_ref: Optional[ActivatedEquipmentRefStructure] = field(
        default=None,
        metadata={
            "name": "EquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    link_ref: Optional[ActivationLinkRefStructure] = field(
        default=None,
        metadata={
            "name": "LinkRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    point_ref: Optional[ActivationPointRefStructure] = field(
        default=None,
        metadata={
            "name": "PointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
