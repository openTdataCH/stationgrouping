from dataclasses import dataclass

from generated.type_of_passenger_information_equipment_value_structure import (
    TypeOfPassengerInformationEquipmentValueStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfPassengerInformationEquipment(
    TypeOfPassengerInformationEquipmentValueStructure
):
    """
    Classification of a PASSENGER INFORMATION EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
