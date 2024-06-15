from dataclasses import dataclass

from generated.equipment_version_structure import EquipmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Equipment(EquipmentVersionStructure):
    """
    An item of EQUIPMENT of a particular type actually available at a location
    within a PLACE, such as QUAY, ACCESS SPACE or STOP PATH LINK.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
