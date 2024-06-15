from dataclasses import dataclass, field
from typing import List, Union

from generated.amount_of_price_unit_product_ref import (
    AmountOfPriceUnitProductRef,
)
from generated.cancelling_ref import CancellingRef
from generated.capped_discount_right_ref import CappedDiscountRightRef
from generated.capping_rule_ref import CappingRuleRef
from generated.charging_policy_ref import ChargingPolicyRef
from generated.commercial_profile_ref import CommercialProfileRef
from generated.companion_profile_ref import CompanionProfileRef
from generated.controllable_element_ref import ControllableElementRef
from generated.customer_purchase_package_element_ref import (
    CustomerPurchasePackageElementRef,
)
from generated.customer_purchase_package_ref import CustomerPurchasePackageRef
from generated.distance_matrix_element_inverse_ref import (
    DistanceMatrixElementInverseRef,
)
from generated.distance_matrix_element_ref import DistanceMatrixElementRef
from generated.eligibility_change_policy_ref import EligibilityChangePolicyRef
from generated.entitlement_given_ref import EntitlementGivenRef
from generated.entitlement_product_ref import EntitlementProductRef
from generated.entitlement_required_ref import EntitlementRequiredRef
from generated.exchanging_ref import ExchangingRef
from generated.fare_demand_factor_ref import FareDemandFactorRef
from generated.fare_product_ref import FareProductRef
from generated.fare_quota_factor_ref import FareQuotaFactorRef
from generated.fare_structure_element_ref import FareStructureElementRef
from generated.frequency_of_use_ref import FrequencyOfUseRef
from generated.fulfilment_method_ref import FulfilmentMethodRef
from generated.geographical_interval_ref import GeographicalIntervalRef
from generated.geographical_structure_factor_ref import (
    GeographicalStructureFactorRef,
)
from generated.group_ticket_ref import GroupTicketRef
from generated.interchanging_ref import InterchangingRef
from generated.luggage_allowance_ref import LuggageAllowanceRef
from generated.minimum_stay_ref import MinimumStayRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.parking_charge_band_ref import ParkingChargeBandRef
from generated.penalty_policy_ref import PenaltyPolicyRef
from generated.preassigned_fare_product_ref import PreassignedFareProductRef
from generated.priceable_object_ref import PriceableObjectRef
from generated.profile_parameter_ref import ProfileParameterRef
from generated.purchase_window_ref import PurchaseWindowRef
from generated.quality_structure_factor_ref import QualityStructureFactorRef
from generated.refunding_ref import RefundingRef
from generated.replacing_ref import ReplacingRef
from generated.reselling_ref import ResellingRef
from generated.reserving_ref import ReservingRef
from generated.round_trip_ref import RoundTripRef
from generated.routing_ref import RoutingRef
from generated.sale_discount_right_ref import SaleDiscountRightRef
from generated.sales_offer_package_element_ref import (
    SalesOfferPackageElementRef,
)
from generated.sales_offer_package_entitlement_given_ref import (
    SalesOfferPackageEntitlementGivenRef,
)
from generated.sales_offer_package_entitlement_required_ref import (
    SalesOfferPackageEntitlementRequiredRef,
)
from generated.sales_offer_package_ref import SalesOfferPackageRef
from generated.series_constraint_ref import SeriesConstraintRef
from generated.service_access_right_ref import ServiceAccessRightRef
from generated.step_limit_ref import StepLimitRef
from generated.subscribing_ref import SubscribingRef
from generated.supplement_product_ref import SupplementProductRef
from generated.suspending_ref import SuspendingRef
from generated.third_party_product_ref import ThirdPartyProductRef
from generated.time_interval_ref import TimeIntervalRef
from generated.time_structure_factor_ref import TimeStructureFactorRef
from generated.transferability_ref import TransferabilityRef
from generated.usage_discount_right_ref import UsageDiscountRightRef
from generated.usage_validity_period_ref import UsageValidityPeriodRef
from generated.user_profile_ref import UserProfileRef
from generated.validable_element_ref import ValidableElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceableObjectRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of PRICEABLE ELEMENTs.
    """

    class Meta:
        name = "priceableObjectRefs_RelStructure"

    choice: List[
        Union[
            CustomerPurchasePackageElementRef,
            CustomerPurchasePackageRef,
            ControllableElementRef,
            ValidableElementRef,
            SalesOfferPackageEntitlementGivenRef,
            SalesOfferPackageEntitlementRequiredRef,
            MinimumStayRef,
            InterchangingRef,
            FrequencyOfUseRef,
            SuspendingRef,
            UsageValidityPeriodRef,
            StepLimitRef,
            RoutingRef,
            RoundTripRef,
            LuggageAllowanceRef,
            EntitlementGivenRef,
            EntitlementRequiredRef,
            EligibilityChangePolicyRef,
            GroupTicketRef,
            CommercialProfileRef,
            CompanionProfileRef,
            UserProfileRef,
            ProfileParameterRef,
            SubscribingRef,
            PenaltyPolicyRef,
            ChargingPolicyRef,
            TransferabilityRef,
            ReplacingRef,
            RefundingRef,
            ExchangingRef,
            ResellingRef,
            CancellingRef,
            ReservingRef,
            PurchaseWindowRef,
            SalesOfferPackageElementRef,
            SalesOfferPackageRef,
            DistanceMatrixElementInverseRef,
            DistanceMatrixElementRef,
            FareStructureElementRef,
            FulfilmentMethodRef,
            SeriesConstraintRef,
            CappingRuleRef,
            EntitlementProductRef,
            SupplementProductRef,
            PreassignedFareProductRef,
            AmountOfPriceUnitProductRef,
            UsageDiscountRightRef,
            ThirdPartyProductRef,
            CappedDiscountRightRef,
            SaleDiscountRightRef,
            FareProductRef,
            ServiceAccessRightRef,
            TimeIntervalRef,
            GeographicalIntervalRef,
            ParkingChargeBandRef,
            TimeStructureFactorRef,
            FareQuotaFactorRef,
            FareDemandFactorRef,
            QualityStructureFactorRef,
            GeographicalStructureFactorRef,
            PriceableObjectRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackageElementRef",
                    "type": CustomerPurchasePackageElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerPurchasePackageRef",
                    "type": CustomerPurchasePackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementRef",
                    "type": ControllableElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementRef",
                    "type": ValidableElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementGivenRef",
                    "type": SalesOfferPackageEntitlementGivenRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementRequiredRef",
                    "type": SalesOfferPackageEntitlementRequiredRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumStayRef",
                    "type": MinimumStayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "InterchangingRef",
                    "type": InterchangingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FrequencyOfUseRef",
                    "type": FrequencyOfUseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SuspendingRef",
                    "type": SuspendingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageValidityPeriodRef",
                    "type": UsageValidityPeriodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StepLimitRef",
                    "type": StepLimitRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoutingRef",
                    "type": RoutingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundTripRef",
                    "type": RoundTripRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageAllowanceRef",
                    "type": LuggageAllowanceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementGivenRef",
                    "type": EntitlementGivenRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementRequiredRef",
                    "type": EntitlementRequiredRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EligibilityChangePolicyRef",
                    "type": EligibilityChangePolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupTicketRef",
                    "type": GroupTicketRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfileRef",
                    "type": CommercialProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionProfileRef",
                    "type": CompanionProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileRef",
                    "type": UserProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ProfileParameterRef",
                    "type": ProfileParameterRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SubscribingRef",
                    "type": SubscribingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PenaltyPolicyRef",
                    "type": PenaltyPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingPolicyRef",
                    "type": ChargingPolicyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransferabilityRef",
                    "type": TransferabilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReplacingRef",
                    "type": ReplacingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RefundingRef",
                    "type": RefundingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ExchangingRef",
                    "type": ExchangingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ResellingRef",
                    "type": ResellingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CancellingRef",
                    "type": CancellingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReservingRef",
                    "type": ReservingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurchaseWindowRef",
                    "type": PurchaseWindowRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageElementRef",
                    "type": SalesOfferPackageElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageRef",
                    "type": SalesOfferPackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementInverseRef",
                    "type": DistanceMatrixElementInverseRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementRef",
                    "type": DistanceMatrixElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementRef",
                    "type": FareStructureElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodRef",
                    "type": FulfilmentMethodRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintRef",
                    "type": SeriesConstraintRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRuleRef",
                    "type": CappingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementProductRef",
                    "type": EntitlementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "ServiceAccessRightRef",
                    "type": ServiceAccessRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalRef",
                    "type": TimeIntervalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalRef",
                    "type": GeographicalIntervalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingChargeBandRef",
                    "type": ParkingChargeBandRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeStructureFactorRef",
                    "type": TimeStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareQuotaFactorRef",
                    "type": FareQuotaFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareDemandFactorRef",
                    "type": FareDemandFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorRef",
                    "type": QualityStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalStructureFactorRef",
                    "type": GeographicalStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PriceableObjectRef",
                    "type": PriceableObjectRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
