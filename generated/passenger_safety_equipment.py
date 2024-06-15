from dataclasses import dataclass

from generated.passenger_safety_equipment_version_structure import (
    PassengerSafetyEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerSafetyEquipment(PassengerSafetyEquipmentVersionStructure):
    """
    Specialisation of PASSENGER EQUIPMENT for passenger safety features, e.g. panic
    button, SOS phone.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
