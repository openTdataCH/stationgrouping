from dataclasses import dataclass

from generated.price_unit_version_structure import PriceUnitVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceUnit(PriceUnitVersionStructure):
    """A unit to express prices: amount of currency, abstract fare unit, ticket unit or token etc."""

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
