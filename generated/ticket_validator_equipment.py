from dataclasses import dataclass

from generated.ticket_validator_equipment_version_structure import (
    TicketValidatorEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TicketValidatorEquipment(TicketValidatorEquipmentVersionStructure):
    """
    Specialisation of INSTALLED EQUIPMENT describing a ticket validator.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
