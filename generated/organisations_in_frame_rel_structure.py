from dataclasses import dataclass, field
from typing import List, Union

from generated.authority import Authority
from generated.containment_aggregation_structure import (
    ContainmentAggregationStructure,
)
from generated.general_organisation import GeneralOrganisation
from generated.management_agent import ManagementAgent
from generated.operator import Operator
from generated.other_organisation import OtherOrganisation
from generated.retail_consortium import RetailConsortium
from generated.serviced_organisation import ServicedOrganisation
from generated.travel_agent import TravelAgent

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OrganisationsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of ORGANISATION.
    """

    class Meta:
        name = "organisationsInFrame_RelStructure"

    choice: List[
        Union[
            RetailConsortium,
            Authority,
            Operator,
            ServicedOrganisation,
            GeneralOrganisation,
            ManagementAgent,
            TravelAgent,
            OtherOrganisation,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RetailConsortium",
                    "type": RetailConsortium,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Authority",
                    "type": Authority,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Operator",
                    "type": Operator,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServicedOrganisation",
                    "type": ServicedOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeneralOrganisation",
                    "type": GeneralOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ManagementAgent",
                    "type": ManagementAgent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TravelAgent",
                    "type": TravelAgent,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OtherOrganisation",
                    "type": OtherOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
