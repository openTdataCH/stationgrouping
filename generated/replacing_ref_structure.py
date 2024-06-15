from dataclasses import dataclass

from generated.reselling_ref_structure import ResellingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReplacingRefStructure(ResellingRefStructure):
    """
    Type for Reference to a REPLACING USAGE PARAMETER.
    """
