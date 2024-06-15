from dataclasses import dataclass

from generated.refunding_version_structure import RefundingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Refunding(RefundingVersionStructure):
    """
    Whether and how the product may be refunded.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
