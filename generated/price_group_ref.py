from dataclasses import dataclass

from generated.price_group_ref_structure import PriceGroupRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceGroupRef(PriceGroupRefStructure):
    """
    Reference to a PRICE GROUP.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
