from dataclasses import dataclass

from generated.access_vehicle_equipment_ref_structure import (
    AccessVehicleEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessVehicleEquipmentRef(AccessVehicleEquipmentRefStructure):
    """
    Reference to an ACCESS VEHICLE EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
