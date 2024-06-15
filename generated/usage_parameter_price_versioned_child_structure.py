from dataclasses import dataclass, field
from typing import Optional, Union

from generated.cancelling_ref import CancellingRef
from generated.charging_policy_ref import ChargingPolicyRef
from generated.commercial_profile_ref import CommercialProfileRef
from generated.companion_profile_ref import CompanionProfileRef
from generated.eligibility_change_policy_ref import EligibilityChangePolicyRef
from generated.entitlement_given_ref import EntitlementGivenRef
from generated.entitlement_required_ref import EntitlementRequiredRef
from generated.exchanging_ref import ExchangingRef
from generated.fare_price_versioned_child_structure import (
    FarePriceVersionedChildStructure,
)
from generated.frequency_of_use_ref import FrequencyOfUseRef
from generated.group_ticket_ref import GroupTicketRef
from generated.interchanging_ref import InterchangingRef
from generated.luggage_allowance_ref import LuggageAllowanceRef
from generated.minimum_stay_ref import MinimumStayRef
from generated.penalty_policy_ref import PenaltyPolicyRef
from generated.profile_parameter_ref import ProfileParameterRef
from generated.purchase_window_ref import PurchaseWindowRef
from generated.refunding_ref import RefundingRef
from generated.replacing_ref import ReplacingRef
from generated.reselling_ref import ResellingRef
from generated.reserving_ref import ReservingRef
from generated.round_trip_ref import RoundTripRef
from generated.routing_ref import RoutingRef
from generated.sales_offer_package_entitlement_given_ref import (
    SalesOfferPackageEntitlementGivenRef,
)
from generated.sales_offer_package_entitlement_required_ref import (
    SalesOfferPackageEntitlementRequiredRef,
)
from generated.step_limit_ref import StepLimitRef
from generated.subscribing_ref import SubscribingRef
from generated.suspending_ref import SuspendingRef
from generated.transferability_ref import TransferabilityRef
from generated.usage_validity_period_ref import UsageValidityPeriodRef
from generated.user_profile_ref import UserProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageParameterPriceVersionedChildStructure(
    FarePriceVersionedChildStructure
):
    """
    Type for a USAGE PARAMETER PRICE.
    """

    class Meta:
        name = "UsageParameterPrice_VersionedChildStructure"

    choice_2: Optional[
        Union[
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
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
