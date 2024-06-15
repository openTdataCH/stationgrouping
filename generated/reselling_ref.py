from dataclasses import dataclass

from generated.reselling_ref_structure import ResellingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ResellingRef(ResellingRefStructure):
    """
    Reference to a RESELLING USAGE PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
