from dataclasses import dataclass

from generated.data_object_service_capabilities_structure import (
    DataObjectServiceCapabilitiesStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DataObjectServiceCapabilities(DataObjectServiceCapabilitiesStructure):
    """
    Capabilities of DataObject Service.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
