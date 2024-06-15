from dataclasses import dataclass

from generated.passenger_equipment_ref_structure import (
    PassengerEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RubbishDisposalEquipmentRefStructure(PassengerEquipmentRefStructure):
    """
    Type for a reference to an RUBBISH DISPOSAL EQUIPMENT.
    """
