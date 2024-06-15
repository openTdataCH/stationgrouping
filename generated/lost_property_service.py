from dataclasses import dataclass

from generated.lost_property_service_version_structure import (
    LostPropertyServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LostPropertyService(LostPropertyServiceVersionStructure):
    """
    Specialisation of CUSTOMER SERVICE for lost properties.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
