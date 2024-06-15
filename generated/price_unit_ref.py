from dataclasses import dataclass

from generated.price_unit_ref_structure import PriceUnitRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceUnitRef(PriceUnitRefStructure):
    """
    Reference to a PRICE UNIT.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
