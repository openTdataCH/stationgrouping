from dataclasses import dataclass

from generated.ticketing_equipment_version_structure import (
    TicketingEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketingEquipment(TicketingEquipmentVersionStructure):
    """
    Specialisation of PASSENGER EQUIPMENT for ticketing.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
