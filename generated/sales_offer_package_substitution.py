from dataclasses import dataclass

from generated.sales_offer_package_substitution_version_structure import (
    SalesOfferPackageSubstitutionVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageSubstitution(
    SalesOfferPackageSubstitutionVersionStructure
):
    """
    A particular tariff, described by a combination of parameters.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
