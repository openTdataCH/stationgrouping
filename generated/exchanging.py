from dataclasses import dataclass

from generated.exchanging_version_structure import ExchangingVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Exchanging(ExchangingVersionStructure):
    """
    The number and characteristics of persons entitled to use the public transport
    service instead of the original customer.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
