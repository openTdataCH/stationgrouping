from dataclasses import dataclass

from generated.communication_service_version_structure import (
    CommunicationServiceVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommunicationService(CommunicationServiceVersionStructure):
    """
    Specialisation of LOCAL SERVICE dedicated to communication services.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
