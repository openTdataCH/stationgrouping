from dataclasses import dataclass, field
from typing import List, Optional, Union

from generated.all_authorities_ref import AllAuthoritiesRef
from generated.all_countries_ref import AllCountriesRef
from generated.all_distribution_channels_ref import AllDistributionChannelsRef
from generated.all_operators_ref import AllOperatorsRef
from generated.all_organisations_ref import AllOrganisationsRef
from generated.all_transport_organisations_ref import (
    AllTransportOrganisationsRef,
)
from generated.amount_of_price_unit_product_ref import (
    AmountOfPriceUnitProductRef,
)
from generated.assignment_version_structure_2 import (
    AssignmentVersionStructure2,
)
from generated.authority_ref import AuthorityRef
from generated.capped_discount_right_ref import CappedDiscountRightRef
from generated.country_ref import CountryRef
from generated.distribution_channel_ref import DistributionChannelRef
from generated.distribution_channel_type_enumeration import (
    DistributionChannelTypeEnumeration,
)
from generated.distribution_rights_enumeration import (
    DistributionRightsEnumeration,
)
from generated.entitlement_product_ref import EntitlementProductRef
from generated.fare_product_ref import FareProductRef
from generated.fulfilment_method_ref import FulfilmentMethodRef
from generated.general_organisation_ref import GeneralOrganisationRef
from generated.group_of_distribution_channels_ref import (
    GroupOfDistributionChannelsRef,
)
from generated.group_of_sales_offer_packages_ref import (
    GroupOfSalesOfferPackagesRef,
)
from generated.management_agent_ref import ManagementAgentRef
from generated.notice_assignments_rel_structure import (
    NoticeAssignmentsRelStructure,
)
from generated.operator_ref import OperatorRef
from generated.organisation_ref import OrganisationRef
from generated.other_organisation_ref import OtherOrganisationRef
from generated.payment_method_enumeration import PaymentMethodEnumeration
from generated.preassigned_fare_product_ref import PreassignedFareProductRef
from generated.responsibility_set_ref import ResponsibilitySetRef
from generated.retail_consortium_ref import RetailConsortiumRef
from generated.sale_discount_right_ref import SaleDiscountRightRef
from generated.sales_offer_package_ref import SalesOfferPackageRef
from generated.service_access_right_ref import ServiceAccessRightRef
from generated.serviced_organisation_ref import ServicedOrganisationRef
from generated.supplement_product_ref import SupplementProductRef
from generated.third_party_product_ref import ThirdPartyProductRef
from generated.ticketing_service_facility_list import (
    TicketingServiceFacilityList,
)
from generated.topographic_place_ref import TopographicPlaceRef
from generated.travel_agent_ref import TravelAgentRef
from generated.usage_discount_right_ref import UsageDiscountRightRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistributionAssignmentVersionStructure(AssignmentVersionStructure2):
    """
    Type for DISTRIBUTION ASSIGNMENT.

    :ivar choice:
    :ivar sales_offer_package_ref:
    :ivar group_of_sales_offer_packages_ref:
    :ivar distribution_rights: Override the folloing   rights allowed by
        channel.
    :ivar all_countries_ref_or_country_ref:
    :ivar allowed_in_country: Whether distribution is allowed or
        forbidden for given country.
    :ivar topographic_place_ref:
    :ivar
        all_distribution_channels_ref_or_group_of_distribution_channels_ref_or_distribution_channel_ref:
    :ivar distribution_channel_type: Classification of  DISTRIBUTION
        CHANNEL.
    :ivar allowed_in_channel: Whether distribution is allowed or
        forbidden for given channel.
    :ivar restricted_to_channel: Whether distribution is restricted to a
        given country and / or channel.
    :ivar mandatory_product: Whether product is mandatory, i.e.  must be
        provided.
    :ivar initial_carrier: Wehther initial carrer has rights.
    :ivar transit_carrier: Whther intremediate transit carrier has
        rights.
    :ivar final_carrier: Whetehr final carrier has rights.
    :ivar choice_1:
    :ivar responsibility_set_ref:
    :ivar ticketing_service_facility_list:
    :ivar payment_methods: Payment methods allowed. May override Channel
        to be more specific.
    :ivar requires_registration: Whetee fDistribution requires the user
        to register.
    :ivar fulfilment_method_ref:
    :ivar notice_assignments: NOTICEs for  SALES PACKAGe.
    """

    class Meta:
        name = "DistributionAssignment_VersionStructure"

    choice: Optional[
        Union[
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
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
            ),
        },
    )
    sales_offer_package_ref: Optional[SalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_of_sales_offer_packages_ref: Optional[
        GroupOfSalesOfferPackagesRef
    ] = field(
        default=None,
        metadata={
            "name": "GroupOfSalesOfferPackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distribution_rights: List[DistributionRightsEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "DistributionRights",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    all_countries_ref_or_country_ref: Optional[
        Union[AllCountriesRef, CountryRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllCountriesRef",
                    "type": AllCountriesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CountryRef",
                    "type": CountryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    allowed_in_country: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllowedInCountry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    topographic_place_ref: Optional[TopographicPlaceRef] = field(
        default=None,
        metadata={
            "name": "TopographicPlaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    all_distribution_channels_ref_or_group_of_distribution_channels_ref_or_distribution_channel_ref: Optional[
        Union[
            AllDistributionChannelsRef,
            GroupOfDistributionChannelsRef,
            DistributionChannelRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllDistributionChannelsRef",
                    "type": AllDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistributionChannelsRef",
                    "type": GroupOfDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionChannelRef",
                    "type": DistributionChannelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    distribution_channel_type: Optional[DistributionChannelTypeEnumeration] = (
        field(
            default=None,
            metadata={
                "name": "DistributionChannelType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    allowed_in_channel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllowedInChannel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    restricted_to_channel: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RestrictedToChannel",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mandatory_product: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MandatoryProduct",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    initial_carrier: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InitialCarrier",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transit_carrier: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TransitCarrier",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    final_carrier: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FinalCarrier",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice_1: Optional[
        Union[
            AllAuthoritiesRef,
            AllOperatorsRef,
            AllTransportOrganisationsRef,
            AllOrganisationsRef,
            RetailConsortiumRef,
            AuthorityRef,
            OperatorRef,
            GeneralOrganisationRef,
            ManagementAgentRef,
            ServicedOrganisationRef,
            TravelAgentRef,
            OtherOrganisationRef,
            OrganisationRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllAuthoritiesRef",
                    "type": AllAuthoritiesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllOperatorsRef",
                    "type": AllOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllTransportOrganisationsRef",
                    "type": AllTransportOrganisationsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllOrganisationsRef",
                    "type": AllOrganisationsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RetailConsortiumRef",
                    "type": RetailConsortiumRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "GeneralOrganisationRef",
                    "type": GeneralOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgentRef",
                    "type": ManagementAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisationRef",
                    "type": ServicedOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgentRef",
                    "type": TravelAgentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisationRef",
                    "type": OtherOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OrganisationRef",
                    "type": OrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    responsibility_set_ref: Optional[ResponsibilitySetRef] = field(
        default=None,
        metadata={
            "name": "ResponsibilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    ticketing_service_facility_list: Optional[TicketingServiceFacilityList] = (
        field(
            default=None,
            metadata={
                "name": "TicketingServiceFacilityList",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    requires_registration: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiresRegistration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fulfilment_method_ref: Optional[FulfilmentMethodRef] = field(
        default=None,
        metadata={
            "name": "FulfilmentMethodRef",
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
