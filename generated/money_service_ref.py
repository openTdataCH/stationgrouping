from dataclasses import dataclass

from generated.money_service_ref_structure import MoneyServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MoneyServiceRef(MoneyServiceRefStructure):
    """
    Identifier of an MONEY SERVICE.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
