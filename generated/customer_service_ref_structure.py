from dataclasses import dataclass

from generated.local_service_ref_structure import LocalServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CustomerServiceRefStructure(LocalServiceRefStructure):
    """
    Type for a reference to an CUSTOMER SERVICE.
    """
