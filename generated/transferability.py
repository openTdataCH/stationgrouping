from dataclasses import dataclass

from generated.transferability_version_structure import (
    TransferabilityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Transferability(TransferabilityVersionStructure):
    """
    The number and characteristics of persons entitled to use the public transport
    service instead of the original customer.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
