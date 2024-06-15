from dataclasses import dataclass

from generated.type_of_entity_version_structure import (
    TypeOfEntityVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfSalesOfferPackageVersionStructure(TypeOfEntityVersionStructure):
    """
    Type for TYPE OF SALES OFFER PACKAGE.
    """

    class Meta:
        name = "TypeOfSalesOfferPackage_VersionStructure"
