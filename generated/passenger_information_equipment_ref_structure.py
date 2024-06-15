from dataclasses import dataclass

from generated.installed_equipment_ref_structure import (
    InstalledEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerInformationEquipmentRefStructure(
    InstalledEquipmentRefStructure
):
    """
    Type for a reference to a PASSENGER INFORMATION EQUIPMENT.
    """
