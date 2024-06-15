from dataclasses import dataclass

from generated.local_service_ref_structure import LocalServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LocalServiceRef(LocalServiceRefStructure):
    """
    Reference to a LOCAL SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
