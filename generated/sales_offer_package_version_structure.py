from dataclasses import dataclass, field
from typing import Optional, Union

from generated.condition_summary import ConditionSummary
from generated.distribution_assignments_rel_structure import (
    DistributionAssignmentsRelStructure,
)
from generated.generic_parameter_assignments_rel_structure import (
    GenericParameterAssignmentsRelStructure,
)
from generated.group_of_sales_offer_package_refs_rel_structure import (
    GroupOfSalesOfferPackageRefsRelStructure,
)
from generated.group_of_sales_offer_packages_ref import (
    GroupOfSalesOfferPackagesRef,
)
from generated.priceable_object_version_structure import (
    PriceableObjectVersionStructure,
)
from generated.private_code import PrivateCode
from generated.rounding_ref import RoundingRef
from generated.sales_offer_package_elements_rel_structure import (
    SalesOfferPackageElementsRelStructure,
)
from generated.sales_offer_package_prices_rel_structure import (
    SalesOfferPackagePricesRelStructure,
)
from generated.sales_offer_package_substitutions_rel_structure import (
    SalesOfferPackageSubstitutionsRelStructure,
)
from generated.type_of_sales_offer_package_ref import (
    TypeOfSalesOfferPackageRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SalesOfferPackageVersionStructure(PriceableObjectVersionStructure):
    """
    Type for SALES OFFER PACKAGE.

    :ivar private_code:
    :ivar type_of_sales_offer_package_ref:
    :ivar condition_summary:
    :ivar validity_parameter_assignments: NOTICE ASSIGNMENTs for  SALES
        OFFER PACKAGE.
    :ivar distribution_assignments:
    :ivar rounding_ref:
    :ivar prices: PRICEs of SALES OFFER PACKAGE ELEMENT.
    :ivar sales_offer_package_elements: SALES OFFER PACKAGE ELEMENTs in
        SALES OFFER PACKAGE.
    :ivar
        group_of_sales_offer_packages_ref_or_groups_of_sale_offer_packages:
    :ivar sales_offer_package_substitutions: SALES TRANSACTIONs in SALES
        OFFER PACKAGE.
    """

    class Meta:
        name = "SalesOfferPackage_VersionStructure"

    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_sales_offer_package_ref: Optional[TypeOfSalesOfferPackageRef] = (
        field(
            default=None,
            metadata={
                "name": "TypeOfSalesOfferPackageRef",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    condition_summary: Optional[ConditionSummary] = field(
        default=None,
        metadata={
            "name": "ConditionSummary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_parameter_assignments: Optional[
        GenericParameterAssignmentsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distribution_assignments: Optional[DistributionAssignmentsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "distributionAssignments",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional[SalesOfferPackagePricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sales_offer_package_elements: Optional[
        SalesOfferPackageElementsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "salesOfferPackageElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_of_sales_offer_packages_ref_or_groups_of_sale_offer_packages: Optional[
        Union[
            GroupOfSalesOfferPackagesRef,
            GroupOfSalesOfferPackageRefsRelStructure,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GroupOfSalesOfferPackagesRef",
                    "type": GroupOfSalesOfferPackagesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "groupsOfSaleOfferPackages",
                    "type": GroupOfSalesOfferPackageRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    sales_offer_package_substitutions: Optional[
        SalesOfferPackageSubstitutionsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "salesOfferPackageSubstitutions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
