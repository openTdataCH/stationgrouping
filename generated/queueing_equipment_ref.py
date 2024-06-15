from dataclasses import dataclass

from generated.access_equipment_ref_structure import (
    AccessEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QueueingEquipmentRef(AccessEquipmentRefStructure):
    """
    Identifier of an QUEUEING EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"