from dataclasses import dataclass

from generated.local_service_ref_structure import LocalServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssistanceBookingServiceRefStructure(LocalServiceRefStructure):
    """
    Type for a reference to an ASSISTANCE BOOKING SERVICE.
    """
