from dataclasses import dataclass, field
from typing import Optional, Union

from generated.addressable_place_version_structure import (
    AddressablePlaceVersionStructure,
)
from generated.authority_ref import AuthorityRef
from generated.contact_structure import ContactStructure
from generated.crew_base_refs_rel_structure import CrewBaseRefsRelStructure
from generated.garage_points_rel_structure import GaragePointsRelStructure
from generated.general_organisation_ref import GeneralOrganisationRef
from generated.management_agent_ref import ManagementAgentRef
from generated.operator_ref import OperatorRef
from generated.organisation_ref import OrganisationRef
from generated.other_organisation_ref import OtherOrganisationRef
from generated.retail_consortium_ref import RetailConsortiumRef
from generated.serviced_organisation_ref import ServicedOrganisationRef
from generated.transport_organisation_refs_rel_structure import (
    TransportOrganisationRefsRelStructure,
)
from generated.travel_agent_ref import TravelAgentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GarageVersionStructure(AddressablePlaceVersionStructure):
    """
    Type for GARAGE.

    :ivar contact_details: Contact details for GARAGE.
    :ivar choice:
    :ivar operators: OPERATORs assoicated with GARAGE.
    :ivar garage_points: GARAGE POINTsin GARAGE
    :ivar crew_bases: CREW BASEs asspicated with GARAGE.
    """

    class Meta:
        name = "Garage_VersionStructure"

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
    operators: Optional[TransportOrganisationRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    garage_points: Optional[GaragePointsRelStructure] = field(
        default=None,
        metadata={
            "name": "garagePoints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    crew_bases: Optional[CrewBaseRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "crewBases",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
