from dataclasses import dataclass, field
from typing import List, Union

from generated.access_vehicle_equipment import AccessVehicleEquipment
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.wheelchair_vehicle_equipment import WheelchairVehicleEquipment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleEquipmentsRelStructure(ContainmentAggregationStructure):
    """
    List of VEHICLE EQUIPMENT.
    """

    class Meta:
        name = "vehicleEquipments_RelStructure"

    access_vehicle_equipment_or_wheelchair_vehicle_equipment: List[
        Union[AccessVehicleEquipment, WheelchairVehicleEquipment]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccessVehicleEquipment",
                    "type": AccessVehicleEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WheelchairVehicleEquipment",
                    "type": WheelchairVehicleEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
