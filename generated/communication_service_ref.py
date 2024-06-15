from dataclasses import dataclass

from generated.communication_service_ref_structure import (
    CommunicationServiceRefStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommunicationServiceRef(CommunicationServiceRefStructure):
    """
    Identifier of an COMMUNICATION SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
