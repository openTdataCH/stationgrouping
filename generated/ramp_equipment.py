from dataclasses import dataclass

from generated.ramp_equipment_version_structure import (
    RampEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RampEquipment(RampEquipmentVersionStructure):
    """
    Specialisation of PLACE ACCESS EQUIPMENT for ramps (provides ramp
    characteristics like length, gradient, etc.).
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
