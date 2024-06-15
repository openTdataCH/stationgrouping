from dataclasses import dataclass

from generated.type_of_retail_device_version_structure import (
    TypeOfRetailDeviceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfRetailDevice(TypeOfRetailDeviceVersionStructure):
    """
    A classification of RETAIL DEVICEs.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
