from dataclasses import dataclass

from generated.vehicle_equipment_ref_structure import (
    VehicleEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WheelchairVehicleRefStructure(VehicleEquipmentRefStructure):
    """
    Type for a reference to a WHEELCHAIR VEHICLE EQUIPMENT.
    """
