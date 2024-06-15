from dataclasses import dataclass, field
from typing import Optional

from generated.activation_assignments_rel_structure import (
    ActivationAssignmentsRelStructure,
)
from generated.equipment_version_structure import EquipmentVersionStructure
from generated.traffic_control_point_ref import TrafficControlPointRef
from generated.type_of_activation_ref import TypeOfActivationRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivatedEquipmentVersionStructure(EquipmentVersionStructure):
    """
    Type for an ACTIVATED EQUIPMENT.

    :ivar traffic_control_point_ref:
    :ivar type_of_activation_ref:
    :ivar assignments: assignments of ACTIVATED EQUIPMENT.
    """

    class Meta:
        name = "ActivatedEquipment_VersionStructure"

    traffic_control_point_ref: Optional[TrafficControlPointRef] = field(
        default=None,
        metadata={
            "name": "TrafficControlPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_activation_ref: Optional[TypeOfActivationRef] = field(
        default=None,
        metadata={
            "name": "TypeOfActivationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    assignments: Optional[ActivationAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
