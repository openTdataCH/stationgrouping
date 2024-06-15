from dataclasses import dataclass

from generated.type_of_passenger_information_equipment_ref_structure import (
    TypeOfPassengerInformationEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfPassengerInformationEquipmentRef(
    TypeOfPassengerInformationEquipmentRefStructure
):
    """
    Reference to a TYPE OF PASSENGER INFORMATION EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
