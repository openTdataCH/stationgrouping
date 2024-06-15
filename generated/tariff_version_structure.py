from dataclasses import dataclass, field
from typing import Optional, Union

from generated.alternative_names_rel_structure import (
    AlternativeNamesRelStructure,
)
from generated.authority_ref import AuthorityRef
from generated.distance_matrix_elements_rel_structure import (
    DistanceMatrixElementsRelStructure,
)
from generated.entity_in_version_structure import DataManagedObjectStructure
from generated.fare_structure_elements_rel_structure import (
    FareStructureElementsRelStructure,
)
from generated.flexible_line_ref import FlexibleLineRef
from generated.general_organisation_ref import GeneralOrganisationRef
from generated.geographical_intervals_rel_structure import (
    GeographicalIntervalsRelStructure,
)
from generated.geographical_structure_factors_rel_structure import (
    GeographicalStructureFactorsRelStructure,
)
from generated.geographical_unit_ref import GeographicalUnitRef
from generated.group_of_lines_ref import GroupOfLinesRef
from generated.group_of_operators_ref import GroupOfOperatorsRef
from generated.groups_of_distance_matrix_elements_rel_structure import (
    GroupsOfDistanceMatrixElementsRelStructure,
)
from generated.info_links_rel_structure import InfoLinksRelStructure
from generated.line_ref import LineRef
from generated.management_agent_ref import ManagementAgentRef
from generated.multilingual_string import MultilingualString
from generated.network_ref import NetworkRef
from generated.notice_assignments_rel_structure import (
    NoticeAssignmentsRelStructure,
)
from generated.operator_ref import OperatorRef
from generated.organisation_ref import OrganisationRef
from generated.other_organisation_ref import OtherOrganisationRef
from generated.price_unit_ref import PriceUnitRef
from generated.priceable_object_version_structure import (
    FareTablesRelStructure,
    PriceGroupsRelStructure,
)
from generated.private_code import PrivateCode
from generated.quality_structure_factors_rel_structure import (
    QualityStructureFactorsRelStructure,
)
from generated.retail_consortium_ref import RetailConsortiumRef
from generated.serviced_organisation_ref import ServicedOrganisationRef
from generated.tariff_basis_enumeration import TariffBasisEnumeration
from generated.time_intervals_rel_structure import TimeIntervalsRelStructure
from generated.time_structure_factors_rel_structure import (
    TimeStructureFactorsRelStructure,
)
from generated.time_unit_ref import TimeUnitRef
from generated.travel_agent_ref import TravelAgentRef
from generated.type_of_tariff_ref import TypeOfTariffRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TariffVersionStructure(DataManagedObjectStructure):
    """
    Type for TARIFF.

    :ivar name: Name of TARIFF.
    :ivar alternative_names: ATERNATIVE NAMEs for TARIFF.
    :ivar description: Description of TARIFF.
    :ivar notice_assignments: NOTICE explaining TARIFF.
    :ivar document_links: Timetable documents associated with the Tariff
        e.g pdf files +v1.1
    :ivar private_code:
    :ivar choice:
    :ivar choice_1:
    :ivar type_of_tariff_ref:
    :ivar tariff_basis: Classification of  Tariff Butasis. Defaut is
        Route (Tap TSI)
    :ivar return_fare_twice_single: Whether return fare is  normally
        twice single fare. Default is true.
    :ivar geographical_unit_ref:
    :ivar geographical_intervals: GEOGRAPHICAL INTERVALs  making up
        TARIFF.
    :ivar geographical_structure_factors: GEOGRAPHICAL STRUCTURE FACTORs
        making up TARIFF.
    :ivar time_unit_ref:
    :ivar time_intervals: VALIDITY PARAMETER ASSIGNMENTs making up
        TARIFF.
    :ivar time_structure_factors: TIME STRUCTURE FACTORs making up
        TARIFF.
    :ivar quality_structure_factors: QUALITY STRUCTURE ELEMENTs making
        up TARIFF.
    :ivar fare_structure_elements: FARE STRUCTURE ELEMENTs making up
        TARIFF.
    :ivar distance_matrix_elements: DISTANCE MATRIX ELEMENTs making up
        TARIFF.
    :ivar groups_of_distance_matrix_elements: GROUPs of DISTANCE MATRIX
        ELEMENTs making up TARIFF.
    :ivar price_unit_ref:
    :ivar price_groups: QUALITY STRUCTURE ELEMENTs making up TARIFF.
    :ivar fare_tables: QUALITY STRUCTURE ELEMENTs making up TARIFF.
    """

    class Meta:
        name = "Tariff_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    alternative_names: Optional[AlternativeNamesRelStructure] = field(
        default=None,
        metadata={
            "name": "alternativeNames",
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
    notice_assignments: Optional[NoticeAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "noticeAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    document_links: Optional[InfoLinksRelStructure] = field(
        default=None,
        metadata={
            "name": "documentLinks",
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
            GroupOfOperatorsRef,
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
                {
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice_1: Optional[
        Union[FlexibleLineRef, LineRef, NetworkRef, GroupOfLinesRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "NetworkRef",
                    "type": NetworkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfLinesRef",
                    "type": GroupOfLinesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_tariff_ref: Optional[TypeOfTariffRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTariffRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tariff_basis: Optional[TariffBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "TariffBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    return_fare_twice_single: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReturnFareTwiceSingle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    geographical_unit_ref: Optional[GeographicalUnitRef] = field(
        default=None,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    geographical_intervals: Optional[GeographicalIntervalsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "geographicalIntervals",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    geographical_structure_factors: Optional[
        GeographicalStructureFactorsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "geographicalStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_unit_ref: Optional[TimeUnitRef] = field(
        default=None,
        metadata={
            "name": "TimeUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_intervals: Optional[TimeIntervalsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeIntervals",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    time_structure_factors: Optional[TimeStructureFactorsRelStructure] = field(
        default=None,
        metadata={
            "name": "timeStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    quality_structure_factors: Optional[
        QualityStructureFactorsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "qualityStructureFactors",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_structure_elements: Optional[FareStructureElementsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "fareStructureElements",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    distance_matrix_elements: Optional[DistanceMatrixElementsRelStructure] = (
        field(
            default=None,
            metadata={
                "name": "distanceMatrixElements",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            },
        )
    )
    groups_of_distance_matrix_elements: Optional[
        GroupsOfDistanceMatrixElementsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "groupsOfDistanceMatrixElements",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    price_unit_ref: Optional[PriceUnitRef] = field(
        default=None,
        metadata={
            "name": "PriceUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    price_groups: Optional[PriceGroupsRelStructure] = field(
        default=None,
        metadata={
            "name": "priceGroups",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_tables: Optional[FareTablesRelStructure] = field(
        default=None,
        metadata={
            "name": "fareTables",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
