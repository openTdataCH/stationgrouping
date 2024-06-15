from dataclasses import dataclass, field
from typing import Optional, Union

from generated.administrative_zones_rel_structure import (
    AdministrativeZonesRelStructure,
)
from generated.authority_ref import AuthorityRef
from generated.contact_structure import ContactStructure
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.general_organisation_ref import GeneralOrganisationRef
from generated.location_structure_2 import LocationStructure2
from generated.management_agent_ref import ManagementAgentRef
from generated.multilingual_string import MultilingualString
from generated.operator_ref import OperatorRef
from generated.organisation_ref import OrganisationRef
from generated.organisation_refs_rel_structure import (
    OrganisationRefsRelStructure,
)
from generated.other_organisation_ref import OtherOrganisationRef
from generated.private_code import PrivateCode
from generated.private_code_structure import PrivateCodeStructure
from generated.responsibility_sets_rel_structure import (
    ResponsibilitySetsRelStructure,
)
from generated.retail_consortium_ref import RetailConsortiumRef
from generated.serviced_organisation_ref import ServicedOrganisationRef
from generated.travel_agent_ref import TravelAgentRef
from generated.type_of_organisation_part_ref import TypeOfOrganisationPartRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationPartVersionStructure(DataManagedObjectStructure):
    """
    Type for an ORGANISATION PART.

    :ivar name: Name of ORGANISATION PART.
    :ivar short_name: Name of DEPARTMENT.
    :ivar description: Name of ORGANISATIONAL UNIT.
    :ivar public_code: Additional public code used for department.
    :ivar private_code:
    :ivar contact_details: Contact details for ORGANISATION PART for
        Public use.
    :ivar location: Coordinates of ORGANISATIONAL UNIT.
    :ivar choice:
    :ivar type_of_organisation_part_ref:
    :ivar administrative_zones: Zones managed by ORGANISATION PART.
    :ivar own_responsibility_sets: Own RESPONSIBILITY SETs V1.1
    :ivar delegated_responsibility_sets: Delegated responsibility SETS.
    :ivar delegated_from: Other Organisations that delegate to this
        Organisation  ORGANISATION. (TAP TSI B1.)
    """

    class Meta:
        name = "OrganisationPart_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
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
    location: Optional[LocationStructure2] = field(
        default=None,
        metadata={
            "name": "Location",
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
    type_of_organisation_part_ref: Optional[TypeOfOrganisationPartRef] = field(
        default=None,
        metadata={
            "name": "TypeOfOrganisationPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    administrative_zones: Optional[AdministrativeZonesRelStructure] = field(
        default=None,
        metadata={
            "name": "administrativeZones",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    own_responsibility_sets: Optional[ResponsibilitySetsRelStructure] = field(
        default=None,
        metadata={
            "name": "ownResponsibilitySets",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    delegated_responsibility_sets: Optional[ResponsibilitySetsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "delegatedResponsibilitySets",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    delegated_from: Optional[OrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "delegatedFrom",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
