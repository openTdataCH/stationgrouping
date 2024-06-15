from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from generated.administrative_zone_ref import AdministrativeZoneRef
from generated.all_vehicle_modes_of_transport_enumeration import (
    AllVehicleModesOfTransportEnumeration,
)
from generated.authority_ref import AuthorityRef
from generated.codespace_assignments_rel_structure import (
    CodespaceAssignmentsRelStructure,
)
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.general_organisation_ref import GeneralOrganisationRef
from generated.management_agent_ref import ManagementAgentRef
from generated.operator_ref import OperatorRef
from generated.organisation_ref import OrganisationRef
from generated.other_organisation_ref import OtherOrganisationRef
from generated.private_code_structure import PrivateCodeStructure
from generated.responsibility_sets_rel_structure import (
    ResponsibilitySetsRelStructure,
)
from generated.retail_consortium_ref import RetailConsortiumRef
from generated.serviced_organisation_ref import ServicedOrganisationRef
from generated.travel_agent_ref import TravelAgentRef
from generated.zone_version_structure import ZoneVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AdministrativeZonesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of ADMINISTRATIVE ZONEs.
    """

    class Meta:
        name = "administrativeZones_RelStructure"

    administrative_zone_ref_or_transport_administrative_zone_or_administrative_zone: List[
        Union[
            AdministrativeZoneRef,
            "TransportAdministrativeZone",
            "AdministrativeZone",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AdministrativeZoneRef",
                    "type": AdministrativeZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportAdministrativeZone",
                    "type": ForwardRef("TransportAdministrativeZone"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AdministrativeZone",
                    "type": ForwardRef("AdministrativeZone"),
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )


@dataclass(kw_only=True)
class AdministrativeZoneVersionStructure(ZoneVersionStructure):
    """
    Type for an ADMINISTRATIVE ZONE.

    :ivar public_code: Public Code assosociated with Zone
    :ivar choice:
    :ivar responsibilities: RESPONSIBILITY SETs allocated to
        ADMINISTRATIVE ZONE.
    :ivar codespace_assignments: CODESPACEs belonging to ADMINISTRATIVE
        ZONE.
    :ivar subzones: Subzones of  ADMINISTRATIVE Zone; ie. strict
        subzones that are administrative subdivisions of the parent.
        These should not contradict Parent ZONE references..
    """

    class Meta:
        name = "AdministrativeZone_VersionStructure"

    public_code: Optional[PrivateCodeStructure] = field(
        default=None,
        metadata={
            "name": "PublicCode",
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
    responsibilities: Optional[ResponsibilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    codespace_assignments: Optional[CodespaceAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "codespaceAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    subzones: Optional[AdministrativeZonesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )


@dataclass(kw_only=True)
class AdministrativeZone(AdministrativeZoneVersionStructure):
    """A ZONE relating to the management responsibilities of an ORGANISATION.

    For example to allocate bus stop identifiers for a region.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportAdministrativeZoneVersionStructure(
    AdministrativeZoneVersionStructure
):
    """
    Type for an TRANSPORT ADMINISTRATIVE  ZONE.

    :ivar vehicle_modes: TRANSPORT MODE for which this zone applies.
        Default is all.
    """

    class Meta:
        name = "TransportAdministrativeZone_VersionStructure"

    vehicle_modes: List[AllVehicleModesOfTransportEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )


@dataclass(kw_only=True)
class TransportAdministrativeZone(TransportAdministrativeZoneVersionStructure):
    """A ZONE relating to the management responsibilities of an ORGANISATION.

    For example to allocate bus stop identifiers for a region.
    """

    class Meta:
        namespace = "http://www.netex.org.uk/netex"
