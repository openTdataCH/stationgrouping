from dataclasses import dataclass

from generated.wheelchair_vehicle_equipment_version_structure import (
    WheelchairVehicleEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WheelchairVehicleEquipment(WheelchairVehicleEquipmentVersionStructure):
    """
    Specialisation of VEHICLE EQUIPMENT for Wheel chair accessibility on board a
    VEHICLE providing information such as the number of wheel chair areas and the
    access dimensions.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
