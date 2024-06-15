from dataclasses import dataclass

from generated.rubbish_disposal_equipment_ref_structure import (
    RubbishDisposalEquipmentRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RubbishDisposalEquipmentRef(RubbishDisposalEquipmentRefStructure):
    """
    Identifier of an RUBBISH DISPOSAL EQUIPMENT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
