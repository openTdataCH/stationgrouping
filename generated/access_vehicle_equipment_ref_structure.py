from dataclasses import dataclass

from generated.vehicle_equipment_ref_structure import (
    VehicleEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessVehicleEquipmentRefStructure(VehicleEquipmentRefStructure):
    """
    Type for a reference to an ACCESS VEHICLE EQUIPMENT.
    """
