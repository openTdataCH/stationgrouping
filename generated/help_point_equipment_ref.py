from dataclasses import dataclass

from generated.help_point_equipment_ref_structure import (
    HelpPointEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HelpPointEquipmentRef(HelpPointEquipmentRefStructure):
    """
    Identifier of an HELP POINT EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
