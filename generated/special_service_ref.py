from dataclasses import dataclass

from generated.special_service_ref_structure import SpecialServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SpecialServiceRef(SpecialServiceRefStructure):
    """
    Reference to a SPECIAL SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
