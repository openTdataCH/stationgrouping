from dataclasses import dataclass

from generated.vehicle_charging_equipment_ref_structure import (
    VehicleChargingEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleChargingEquipmentRef(VehicleChargingEquipmentRefStructure):
    """
    Identifier of an VEHICLE CHARGING EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
