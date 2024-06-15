from dataclasses import dataclass

from generated.sanitary_equipment_version_structure import (
    SanitaryEquipmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SanitaryEquipment(SanitaryEquipmentVersionStructure):
    """
    A SANITARY FACILITY , e.g. WC, Shower, baby change.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
