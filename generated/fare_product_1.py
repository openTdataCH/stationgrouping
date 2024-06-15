from dataclasses import dataclass

from generated.fare_product_version_structure import (
    FareProductVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareProduct1(FareProductVersionStructure):
    """
    An immaterial marketable element (access rights, discount rights etc), specific
    to a CHARGING MOMENT.
    """

    class Meta:
        name = "FareProduct"
        namespace = "http://www.netex.org.uk/netex"
