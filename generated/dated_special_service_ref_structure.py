from dataclasses import dataclass

from generated.special_service_ref_structure import SpecialServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DatedSpecialServiceRefStructure(SpecialServiceRefStructure):
    """
    Type for a reference to a DATED SPECIAL SERVICE.
    """
