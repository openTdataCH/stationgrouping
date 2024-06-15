from dataclasses import dataclass, field
from typing import List, Union

from generated.cancelling import Cancelling
from generated.cancelling_ref import CancellingRef
from generated.charging_policy import ChargingPolicy
from generated.charging_policy_ref import ChargingPolicyRef
from generated.commercial_profile import CommercialProfile
from generated.commercial_profile_ref import CommercialProfileRef
from generated.companion_profile import CompanionProfile
from generated.companion_profile_ref import CompanionProfileRef
from generated.eligibility_change_policy import EligibilityChangePolicy
from generated.eligibility_change_policy_ref import EligibilityChangePolicyRef
from generated.entitlement_given import EntitlementGiven
from generated.entitlement_given_ref import EntitlementGivenRef
from generated.entitlement_required import EntitlementRequired
from generated.entitlement_required_ref import EntitlementRequiredRef
from generated.exchanging import Exchanging
from generated.exchanging_ref import ExchangingRef
from generated.frequency_of_use import FrequencyOfUse
from generated.frequency_of_use_ref import FrequencyOfUseRef
from generated.group_ticket import GroupTicket
from generated.group_ticket_ref import GroupTicketRef
from generated.interchanging import Interchanging
from generated.interchanging_ref import InterchangingRef
from generated.luggage_allowance import LuggageAllowance
from generated.luggage_allowance_ref import LuggageAllowanceRef
from generated.minimum_stay import MinimumStay
from generated.minimum_stay_ref import MinimumStayRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.penalty_policy import PenaltyPolicy
from generated.penalty_policy_ref import PenaltyPolicyRef
from generated.profile_parameter_ref import ProfileParameterRef
from generated.purchase_window import PurchaseWindow
from generated.purchase_window_ref import PurchaseWindowRef
from generated.refunding import Refunding
from generated.refunding_ref import RefundingRef
from generated.replacing import Replacing
from generated.replacing_ref import ReplacingRef
from generated.reselling import Reselling
from generated.reselling_ref import ResellingRef
from generated.reserving import Reserving
from generated.reserving_ref import ReservingRef
from generated.round_trip import RoundTrip
from generated.round_trip_ref import RoundTripRef
from generated.routing import Routing
from generated.routing_ref import RoutingRef
from generated.sales_offer_package_entitlement_given import (
    SalesOfferPackageEntitlementGiven,
)
from generated.sales_offer_package_entitlement_given_ref import (
    SalesOfferPackageEntitlementGivenRef,
)
from generated.sales_offer_package_entitlement_required import (
    SalesOfferPackageEntitlementRequired,
)
from generated.sales_offer_package_entitlement_required_ref import (
    SalesOfferPackageEntitlementRequiredRef,
)
from generated.step_limit import StepLimit
from generated.step_limit_ref import StepLimitRef
from generated.subscribing import Subscribing
from generated.subscribing_ref import SubscribingRef
from generated.suspending import Suspending
from generated.suspending_ref import SuspendingRef
from generated.transferability import Transferability
from generated.transferability_ref import TransferabilityRef
from generated.usage_validity_period import UsageValidityPeriod
from generated.usage_validity_period_ref import UsageValidityPeriodRef
from generated.user_profile import UserProfile
from generated.user_profile_ref import UserProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageParametersRelStructure(OneToManyRelationshipStructure):
    """
    Type for of USAGE PARAMETER.
    """

    class Meta:
        name = "usageParameters_RelStructure"

    choice: List[
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
            SalesOfferPackageEntitlementRequired,
            SalesOfferPackageEntitlementGiven,
            MinimumStay,
            Interchanging,
            Suspending,
            UsageValidityPeriod,
            FrequencyOfUse,
            StepLimit,
            Routing,
            RoundTrip,
            LuggageAllowance,
            EntitlementRequired,
            EntitlementGiven,
            EligibilityChangePolicy,
            CompanionProfile,
            GroupTicket,
            CommercialProfile,
            UserProfile,
            Subscribing,
            PenaltyPolicy,
            ChargingPolicy,
            Cancelling,
            Reserving,
            PurchaseWindow,
            Transferability,
            Replacing,
            Refunding,
            Exchanging,
            Reselling,
        ]
    ] = field(
        default_factory=list,
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
                {
                    "name": "SalesOfferPackageEntitlementRequired",
                    "type": SalesOfferPackageEntitlementRequired,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackageEntitlementGiven",
                    "type": SalesOfferPackageEntitlementGiven,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MinimumStay",
                    "type": MinimumStay,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Interchanging",
                    "type": Interchanging,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Suspending",
                    "type": Suspending,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageValidityPeriod",
                    "type": UsageValidityPeriod,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FrequencyOfUse",
                    "type": FrequencyOfUse,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StepLimit",
                    "type": StepLimit,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Routing",
                    "type": Routing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RoundTrip",
                    "type": RoundTrip,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LuggageAllowance",
                    "type": LuggageAllowance,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementRequired",
                    "type": EntitlementRequired,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EntitlementGiven",
                    "type": EntitlementGiven,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EligibilityChangePolicy",
                    "type": EligibilityChangePolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CompanionProfile",
                    "type": CompanionProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupTicket",
                    "type": GroupTicket,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CommercialProfile",
                    "type": CommercialProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfile",
                    "type": UserProfile,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Subscribing",
                    "type": Subscribing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PenaltyPolicy",
                    "type": PenaltyPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChargingPolicy",
                    "type": ChargingPolicy,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Cancelling",
                    "type": Cancelling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Reserving",
                    "type": Reserving,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PurchaseWindow",
                    "type": PurchaseWindow,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Transferability",
                    "type": Transferability,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Replacing",
                    "type": Replacing,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Refunding",
                    "type": Refunding,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Exchanging",
                    "type": Exchanging,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Reselling",
                    "type": Reselling,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
