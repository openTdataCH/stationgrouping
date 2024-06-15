from dataclasses import dataclass, field
from typing import List, Optional, Union

from generated.alternative_names_rel_structure import (
    AlternativeNamesRelStructure,
)
from generated.authority_ref import AuthorityRef
from generated.contact_structure import ContactStructure
from generated.distribution_channel_type_enumeration import (
    DistributionChannelTypeEnumeration,
)
from generated.distribution_rights_enumeration import (
    DistributionRightsEnumeration,
)
from generated.general_group_of_entities_ref_structure import (
    GeneralGroupOfEntitiesRefStructure,
)
from generated.general_organisation_ref import GeneralOrganisationRef
from generated.management_agent_ref import ManagementAgentRef
from generated.operator_ref import OperatorRef
from generated.organisation_ref import OrganisationRef
from generated.other_organisation_ref import OtherOrganisationRef
from generated.payment_method_enumeration import PaymentMethodEnumeration
from generated.point_refs_rel_structure import PointRefsRelStructure
from generated.retail_consortium_ref import RetailConsortiumRef
from generated.serviced_organisation_ref import ServicedOrganisationRef
from generated.travel_agent_ref import TravelAgentRef
from generated.type_of_payment_method_refs_rel_structure import (
    TypeOfPaymentMethodRefsRelStructure,
)
from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DistributionChannelVersionStructure(TypeOfValueVersionStructure):
    """
    Type for DISTRIBUTION CHANNEL.

    :ivar alternative_names: SALES TRANSACTIONs in DISTRIBUTION CHANNEL.
    :ivar distribution_channel_type: Classification of  DISTRIBUTION
        CHANNEL.
    :ivar is_obligatory: Whether use of the channel is obligatory.
    :ivar requires_email_address: Whether use of the channel requries
        the pruchaser to have an email address.
    :ivar contact_details: Contact details for distribution channel
    :ivar choice:
    :ivar payment_methods: Payment methods allowed.
    :ivar types_of_payment_method: Additional methods for paymen + v1.1
    :ivar distribution_rights: Defaut distribution Rigts allowed by
        DISTRIBUTION CHANNEL.
    :ivar distribution_points_or_distribution_group_ref:
    """

    class Meta:
        name = "DistributionChannel_VersionStructure"

    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    is_obligatory: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsObligatory",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    requires_email_address: Optional[bool] = field(
        default=None,
        metadata={
            "name": "RequiresEmailAddress",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    contact_details: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "ContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
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
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    types_of_payment_method: Optional[TypeOfPaymentMethodRefsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "typesOfPaymentMethod",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
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
    distribution_points_or_distribution_group_ref: Optional[
        Union[PointRefsRelStructure, GeneralGroupOfEntitiesRefStructure]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "distributionPoints",
                    "type": PointRefsRelStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistributionGroupRef",
                    "type": GeneralGroupOfEntitiesRefStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
