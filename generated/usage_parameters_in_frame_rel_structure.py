from dataclasses import dataclass, field
from typing import List, Union

from generated.cancelling import Cancelling
from generated.charging_policy import ChargingPolicy
from generated.commercial_profile import CommercialProfile
from generated.companion_profile import CompanionProfile
from generated.eligibility_change_policy import EligibilityChangePolicy
from generated.entitlement_given import EntitlementGiven
from generated.entitlement_required import EntitlementRequired
from generated.exchanging import Exchanging
from generated.frame_containment_structure import FrameContainmentStructure
from generated.frequency_of_use import FrequencyOfUse
from generated.group_ticket import GroupTicket
from generated.interchanging import Interchanging
from generated.luggage_allowance import LuggageAllowance
from generated.minimum_stay import MinimumStay
from generated.penalty_policy import PenaltyPolicy
from generated.purchase_window import PurchaseWindow
from generated.refunding import Refunding
from generated.replacing import Replacing
from generated.reselling import Reselling
from generated.reserving import Reserving
from generated.round_trip import RoundTrip
from generated.routing import Routing
from generated.sales_offer_package_entitlement_given import (
    SalesOfferPackageEntitlementGiven,
)
from generated.sales_offer_package_entitlement_required import (
    SalesOfferPackageEntitlementRequired,
)
from generated.step_limit import StepLimit
from generated.subscribing import Subscribing
from generated.suspending import Suspending
from generated.transferability import Transferability
from generated.usage_validity_period import UsageValidityPeriod
from generated.user_profile import UserProfile

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class UsageParametersInFrameRelStructure(FrameContainmentStructure):
    """
    Type for containment in frame of USAGE PARAMETER.
    """

    class Meta:
        name = "usageParametersInFrame_RelStructure"

    choice: List[
        Union[
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
