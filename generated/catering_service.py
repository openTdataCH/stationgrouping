from dataclasses import dataclass

from generated.catering_service_version_structure import (
    CateringServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CateringService(CateringServiceVersionStructure):
    """
    Specialisation of LOCAL SERVICE dedicated to catering service.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
