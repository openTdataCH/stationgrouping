from dataclasses import dataclass, field
from typing import Optional, Union

from generated.alternative_names_rel_structure import (
    AlternativeNamesRelStructure,
)
from generated.condition_summary import ConditionSummary
from generated.discounting_rule_ref import DiscountingRuleRef
from generated.distribution_assignments_rel_structure import (
    DistributionAssignmentsRelStructure,
)
from generated.generic_parameter_assignments_rel_structure import (
    GenericParameterAssignmentsRelStructure,
)
from generated.group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from generated.limiting_rule_ref import LimitingRuleRef
from generated.notice_assignments_rel_structure import (
    NoticeAssignmentsRelStructure,
)
from generated.priceable_object_version_structure import (
    FareTablesRelStructure,
    PriceGroupsRelStructure,
)
from generated.pricing_rule_ref import PricingRuleRef
from generated.pricing_service_ref import PricingServiceRef
from generated.rounding_ref import RoundingRef
from generated.sales_offer_package_elements_rel_structure import (
    SalesOfferPackageElementsRelStructure,
)
from generated.sales_offer_package_prices_rel_structure import (
    SalesOfferPackagePricesRelStructure,
)
from generated.sales_offer_package_refs_rel_structure import (
    SalesOfferPackageRefsRelStructure,
)
from generated.type_of_sales_offer_package_ref import (
    TypeOfSalesOfferPackageRef,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfSalesOfferPackagesVersionStructure(
    GroupOfEntitiesVersionStructure
):
    """
    Type for GROUP OF SALES OFFER PACKAGEs.

    :ivar alternative_names: ALTERNATIVE NAMEs for PRICEABLE OBJECT.
    :ivar notice_assignments: NOTICE ASSIGNMENTs for PRICEABLE OBJECT.
    :ivar pricing_service_ref:
    :ivar limiting_rule_ref_or_discounting_rule_ref_or_pricing_rule_ref:
    :ivar price_groups: PRICE GROUPSs  making up FARE PRODUCT.
    :ivar fare_tables: Other FARE TABLESs for DISTANCE MATRIX ELEMENT.
    :ivar type_of_sales_offer_package_ref:
    :ivar condition_summary:
    :ivar validity_parameter_assignments: NOTICE ASSIGNMENTs for  SALES
        OFFER PACKAGE.
    :ivar distribution_assignments:
    :ivar rounding_ref:
    :ivar prices: PRICEs of SALES OFFER PACKAGE ELEMENT.
    :ivar sales_offer_package_elements: SALES OFFER PACKAGE ELEMENTs in
        SALES OFFER PACKAGE.
    :ivar members: SALES OFFER PACKAGEs in Group.
    """

    class Meta:
        name = "GroupOfSalesOfferPackages_VersionStructure"

    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    pricing_service_ref: Optional[PricingServiceRef] = field(
        default=None,
        metadata={
            "name": "PricingServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    limiting_rule_ref_or_discounting_rule_ref_or_pricing_rule_ref: Optional[
        Union[LimitingRuleRef, DiscountingRuleRef, PricingRuleRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LimitingRuleRef",
                    "type": LimitingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRuleRef",
                    "type": DiscountingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRuleRef",
                    "type": PricingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    price_groups: Optional[PriceGroupsRelStructure] = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_tables: Optional[FareTablesRelStructure] = field(
        default=None,
        metadata={
            "name": "fareTables",
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
    members: Optional[SalesOfferPackageRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
