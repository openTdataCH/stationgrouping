from dataclasses import dataclass

from generated.refunding_ref_structure import RefundingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RefundingRef(RefundingRefStructure):
    """
    Reference to a REFUNDING USAGE PARAMETER.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
