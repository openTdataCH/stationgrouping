from dataclasses import dataclass

from generated.vehicle_charging_equipment_version_structure import (
    VehicleChargingEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleChargingEquipment(VehicleChargingEquipmentVersionStructure):
    """
    Specialisation of PLACE EQUIPMENT for vehicle charging.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
