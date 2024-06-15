from dataclasses import dataclass

from generated.activated_equipment_version_structure import (
    ActivatedEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivatedEquipment(ActivatedEquipmentVersionStructure):
    """
    An EQUIPMENT activated by the passage of a vehicle at an ACTIVATION POINT or on
    an ACTIVATION LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
