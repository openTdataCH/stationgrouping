from dataclasses import dataclass

from generated.access_vehicle_equipment_version_structure import (
    AccessVehicleEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AccessVehicleEquipment(AccessVehicleEquipmentVersionStructure):
    """
    Specialisation of VEHICLE EQUIPMENT for ACCESS providing information such as
    low floor, ramp, access area dimensions, etc.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
