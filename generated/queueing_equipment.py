from dataclasses import dataclass

from generated.queueing_equipment_version_structure import (
    QueueingEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class QueueingEquipment(QueueingEquipmentVersionStructure):
    """
    Specialisation of PLACE ACCESS EQUIPMENT dedicated to queuing.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
