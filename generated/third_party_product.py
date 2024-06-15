from dataclasses import dataclass

from generated.third_party_product_version_structure import (
    ThirdPartyProductVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ThirdPartyProduct(ThirdPartyProductVersionStructure):
    """
    A FARE PRODUCT that is marketed together with a Public Transport Fare Product.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
