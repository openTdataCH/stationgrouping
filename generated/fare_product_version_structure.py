from dataclasses import dataclass, field
from typing import Optional, Union

from generated.access_rights_in_product_rel_structure import (
    AccessRightsInProductRelStructure,
)
from generated.amount_of_price_unit_product_ref import (
    AmountOfPriceUnitProductRef,
)
from generated.authority_ref import AuthorityRef
from generated.capped_discount_right_ref import CappedDiscountRightRef
from generated.charging_moment_enumeration import ChargingMomentEnumeration
from generated.charging_moment_ref import ChargingMomentRef
from generated.condition_summary import ConditionSummary
from generated.fare_product_prices_rel_structure import (
    FareProductPricesRelStructure,
)
from generated.fare_product_ref import FareProductRef
from generated.generic_parameter_assignments_rel_structure import (
    GenericParameterAssignment,
    GenericParameterAssignmentInContext,
    GenericParameterAssignmentsRelStructure,
)
from generated.operator_ref import OperatorRef
from generated.preassigned_fare_product_ref import PreassignedFareProductRef
from generated.sale_discount_right_ref import SaleDiscountRightRef
from generated.service_access_right_version_structure import (
    ServiceAccessRightVersionStructure,
)
from generated.supplement_product_ref import SupplementProductRef
from generated.tariff_refs_rel_structure import TariffRefsRelStructure
from generated.third_party_product_ref import ThirdPartyProductRef
from generated.type_of_fare_product_ref import TypeOfFareProductRef
from generated.type_of_fare_product_refs_rel_structure import (
    TypeOfFareProductRefsRelStructure,
)
from generated.usage_discount_right_ref import UsageDiscountRightRef
from generated.validable_elements_rel_structure import (
    ValidableElementsRelStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareProductVersionStructure(ServiceAccessRightVersionStructure):
    """
    Type for FARE PRODUCT.

    :ivar charging_moment_ref:
    :ivar charging_moment_type: Enumeration of standardised Charging
        moment values _v1.1
    :ivar type_of_fare_product_ref_or_types_of_fare_product:
    :ivar authority_ref_or_operator_ref:
    :ivar condition_summary:
    :ivar choice:
    :ivar
        validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context:
    :ivar validable_elements: VALIDABLE ELEMENTs making up FARE SERVICE
        ACCESS RIGHT.
    :ivar access_rights_in_product: Access rights given by product.
    :ivar tariffs: TARIFFs  used by FARE PRODUCT. These may be derived
        from lower level references.
    :ivar prices: PRICEs  making up FARE PRODUCT.
    """

    class Meta:
        name = "FareProduct_VersionStructure"

    charging_moment_ref: Optional[ChargingMomentRef] = field(
        default=None,
        metadata={
            "name": "ChargingMomentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    charging_moment_type: Optional[ChargingMomentEnumeration] = field(
        default=None,
        metadata={
            "name": "ChargingMomentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_fare_product_ref_or_types_of_fare_product: Optional[
        Union[TypeOfFareProductRef, TypeOfFareProductRefsRelStructure]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfFareProductRef",
                    "type": TypeOfFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "typesOfFareProduct",
                    "type": TypeOfFareProductRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    authority_ref_or_operator_ref: Optional[
        Union[AuthorityRef, OperatorRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    condition_summary: Optional[ConditionSummary] = field(
        default=None,
        metadata={
            "name": "ConditionSummary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            SupplementProductRef,
            PreassignedFareProductRef,
            AmountOfPriceUnitProductRef,
            UsageDiscountRightRef,
            ThirdPartyProductRef,
            CappedDiscountRightRef,
            SaleDiscountRightRef,
            FareProductRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplementProductRef",
                    "type": SupplementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProductRef",
                    "type": PreassignedFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProductRef",
                    "type": AmountOfPriceUnitProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRightRef",
                    "type": UsageDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProductRef",
                    "type": ThirdPartyProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRightRef",
                    "type": CappedDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRightRef",
                    "type": SaleDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductRef",
                    "type": FareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    validity_parameter_assignments_or_generic_parameter_assignment_or_generic_parameter_assignment_in_context: Optional[
        Union[
            GenericParameterAssignmentsRelStructure,
            GenericParameterAssignment,
            GenericParameterAssignmentInContext,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "validityParameterAssignments",
                    "type": GenericParameterAssignmentsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignment",
                    "type": GenericParameterAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GenericParameterAssignmentInContext",
                    "type": GenericParameterAssignmentInContext,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    validable_elements: Optional[ValidableElementsRelStructure] = field(
        default=None,
        metadata={
            "name": "validableElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_rights_in_product: Optional[AccessRightsInProductRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "accessRightsInProduct",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    tariffs: Optional[TariffRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices: Optional[FareProductPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
