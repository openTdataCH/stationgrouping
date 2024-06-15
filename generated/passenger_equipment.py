from dataclasses import dataclass

from generated.passenger_equipment_version_structure import (
    PassengerEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerEquipment(PassengerEquipmentVersionStructure):
    """
    Equipment for passengers that may be in a fixed within a STOP PLACE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
