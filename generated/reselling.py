from dataclasses import dataclass

from generated.reselling_version_structure import ResellingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Reselling(ResellingVersionStructure):
    """
    Common resale conditions (i.e. for exchange or refund)  attaching to the
    product.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
