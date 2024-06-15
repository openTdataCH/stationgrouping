from dataclasses import dataclass

from generated.access_equipment_ref_structure import (
    AccessEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RampEquipmentRef(AccessEquipmentRefStructure):
    """
    Identifier of an RAMP EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
