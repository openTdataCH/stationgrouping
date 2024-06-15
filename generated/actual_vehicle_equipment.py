from dataclasses import dataclass

from generated.actual_vehicle_equipment_version_structure import (
    ActualVehicleEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActualVehicleEquipment(ActualVehicleEquipmentVersionStructure):
    """
    An item of EQUIPMENT of a particular type actually available in an individual
    VEHICLE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
