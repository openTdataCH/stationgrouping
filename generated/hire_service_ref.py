from dataclasses import dataclass

from generated.hire_service_ref_structure import HireServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HireServiceRef(HireServiceRefStructure):
    """
    Identifier of an HIRE SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
