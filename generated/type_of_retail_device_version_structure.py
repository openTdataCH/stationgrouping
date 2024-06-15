from dataclasses import dataclass

from generated.type_of_entity_version_structure import (
    TypeOfEntityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfRetailDeviceVersionStructure(TypeOfEntityVersionStructure):
    """
    Type for TYPE OF RETAIL DEVICE.
    """

    class Meta:
        name = "TypeOfRetailDevice_VersionStructure"
