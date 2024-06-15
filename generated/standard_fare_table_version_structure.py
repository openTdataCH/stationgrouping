from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from xsdata.models.datatype import XmlDate

from generated.authority_ref import AuthorityRef
from generated.general_organisation_ref import GeneralOrganisationRef
from generated.group_of_entities_version_structure import (
    GroupOfEntitiesVersionStructure,
)
from generated.management_agent_ref import ManagementAgentRef
from generated.operator_ref import OperatorRef
from generated.organisation_ref import OrganisationRef
from generated.other_organisation_ref import OtherOrganisationRef
from generated.priceable_object_refs_rel_structure import (
    PriceableObjectRefsRelStructure,
)
from generated.retail_consortium_ref import RetailConsortiumRef
from generated.rounding_ref import RoundingRef
from generated.serviced_organisation_ref import ServicedOrganisationRef
from generated.travel_agent_ref import TravelAgentRef
from generated.type_of_fare_table_ref import TypeOfFareTableRef
from generated.used_in_refs_rel_structure import UsedInRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class StandardFareTableVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for a STANDARD FARE TABLE PRICE GROUP.

    :ivar start_date: Start date for PRICE GROUP.
    :ivar end_date: End date for PRICE GROUP.
    :ivar rounding_ref:
    :ivar type_of_fare_table_ref:
    :ivar prices_for: Combination of Elements for which this table
        provides PRICEs.
    :ivar used_in: Elements that use FARE TABLE that are not PRICEABLE
        OBJECTs.
    :ivar choice:
    :ivar first_class_single: Price for a first class single  fare.
    :ivar second_class_single: Price for a second class  single fare.
    :ivar first_class_return: Price for a first class return fare.
    :ivar second_class_return: Price for a second class return fare.
    """

    class Meta:
        name = "StandardFareTable_VersionStructure"

    start_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "StartDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "EndDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rounding_ref: Optional[RoundingRef] = field(
        default=None,
        metadata={
            "name": "RoundingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_fare_table_ref: Optional[TypeOfFareTableRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareTableRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    prices_for: Optional[PriceableObjectRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "pricesFor",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    used_in: Optional[UsedInRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "usedIn",
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
    first_class_single: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FirstClassSingle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    second_class_single: Decimal = field(
        metadata={
            "name": "SecondClassSingle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    first_class_return: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FirstClassReturn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    second_class_return: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "SecondClassReturn",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
