from dataclasses import dataclass, field
from typing import List, Union

from generated.access_vehicle_equipment_ref import AccessVehicleEquipmentRef
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.help_point_equipment import HelpPointEquipment
from generated.help_point_equipment_ref import HelpPointEquipmentRef
from generated.passenger_equipment_ref import PassengerEquipmentRef
from generated.passenger_information_equipment import (
    PassengerInformationEquipment,
)
from generated.passenger_safety_equipment import PassengerSafetyEquipment
from generated.passenger_safety_equipment_ref import (
    PassengerSafetyEquipmentRef,
)
from generated.rubbish_disposal_equipment import RubbishDisposalEquipment
from generated.rubbish_disposal_equipment_ref import (
    RubbishDisposalEquipmentRef,
)
from generated.sanitary_equipment import SanitaryEquipment
from generated.sanitary_equipment_ref import SanitaryEquipmentRef
from generated.vehicle_equipment_ref import VehicleEquipmentRef
from generated.wheelchair_vehicle_ref import WheelchairVehicleRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerEquipmentsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of LOCAL SERVICEs.
    """

    class Meta:
        name = "passengerEquipments_RelStructure"

    choice: List[
        Union[
            RubbishDisposalEquipmentRef,
            HelpPointEquipmentRef,
            PassengerSafetyEquipmentRef,
            SanitaryEquipmentRef,
            WheelchairVehicleRef,
            AccessVehicleEquipmentRef,
            VehicleEquipmentRef,
            PassengerEquipmentRef,
            PassengerInformationEquipment,
            RubbishDisposalEquipment,
            HelpPointEquipment,
            PassengerSafetyEquipment,
            SanitaryEquipment,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RubbishDisposalEquipmentRef",
                    "type": RubbishDisposalEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HelpPointEquipmentRef",
                    "type": HelpPointEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSafetyEquipmentRef",
                    "type": PassengerSafetyEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SanitaryEquipmentRef",
                    "type": SanitaryEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WheelchairVehicleRef",
                    "type": WheelchairVehicleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessVehicleEquipmentRef",
                    "type": AccessVehicleEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleEquipmentRef",
                    "type": VehicleEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerEquipmentRef",
                    "type": PassengerEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerInformationEquipment",
                    "type": PassengerInformationEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RubbishDisposalEquipment",
                    "type": RubbishDisposalEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "HelpPointEquipment",
                    "type": HelpPointEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PassengerSafetyEquipment",
                    "type": PassengerSafetyEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SanitaryEquipment",
                    "type": SanitaryEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
