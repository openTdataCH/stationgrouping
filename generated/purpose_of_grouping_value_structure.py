from dataclasses import dataclass, field
from typing import Optional, Union

from generated.class_refs_rel_structure import ClassRefsRelStructure
from generated.customer_account_status import CustomerAccountStatus
from generated.type_of_access_right_assignment import (
    TypeOfAccessRightAssignment,
)
from generated.type_of_activation import TypeOfActivation
from generated.type_of_congestion import TypeOfCongestion
from generated.type_of_customer_account import TypeOfCustomerAccount
from generated.type_of_delivery_variant import TypeOfDeliveryVariant
from generated.type_of_entity import TypeOfEntity
from generated.type_of_equipment import TypeOfEquipment
from generated.type_of_facility import TypeOfFacility
from generated.type_of_fare_contract import TypeOfFareContract
from generated.type_of_fare_contract_entry import TypeOfFareContractEntry
from generated.type_of_fare_product import TypeOfFareProduct
from generated.type_of_fare_structure_element import TypeOfFareStructureElement
from generated.type_of_fare_structure_factor import TypeOfFareStructureFactor
from generated.type_of_feature import TypeOfFeature
from generated.type_of_flexible_service import TypeOfFlexibleService
from generated.type_of_journey_pattern import TypeOfJourneyPattern
from generated.type_of_line import TypeOfLine
from generated.type_of_link import TypeOfLink
from generated.type_of_link_sequence import TypeOfLinkSequence
from generated.type_of_notice import TypeOfNotice
from generated.type_of_operation import TypeOfOperation
from generated.type_of_organisation import TypeOfOrganisation
from generated.type_of_organisation_part import TypeOfOrganisationPart
from generated.type_of_passenger_information_equipment import (
    TypeOfPassengerInformationEquipment,
)
from generated.type_of_place import TypeOfPlace
from generated.type_of_point import TypeOfPoint
from generated.type_of_projection import TypeOfProjection
from generated.type_of_responsibility_role import TypeOfResponsibilityRole
from generated.type_of_retail_device import TypeOfRetailDevice
from generated.type_of_sales_offer_package import TypeOfSalesOfferPackage
from generated.type_of_service import TypeOfService
from generated.type_of_tariff import TypeOfTariff
from generated.type_of_time_demand_type import TypeOfTimeDemandType
from generated.type_of_transfer import TypeOfTransfer
from generated.type_of_travel_document import TypeOfTravelDocument
from generated.type_of_value_version_structure import (
    TypeOfValueVersionStructure,
)
from generated.type_of_zone import TypeOfZone
from generated.types_of_frame_rel_structure import TypeOfFrame

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurposeOfGroupingValueStructure(TypeOfValueVersionStructure):
    """
    Type for a PURPOSE OF GROUPING.

    :ivar classes: Allowed class types for grouping.
    :ivar choice:
    """

    class Meta:
        name = "PurposeOfGrouping_ValueStructure"

    classes: Optional[ClassRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            TypeOfRetailDevice,
            CustomerAccountStatus,
            TypeOfCustomerAccount,
            TypeOfFareContractEntry,
            TypeOfFareContract,
            TypeOfTravelDocument,
            TypeOfSalesOfferPackage,
            TypeOfFareProduct,
            TypeOfFareStructureElement,
            TypeOfTariff,
            TypeOfAccessRightAssignment,
            TypeOfFareStructureFactor,
            TypeOfFlexibleService,
            TypeOfTimeDemandType,
            TypeOfPassengerInformationEquipment,
            TypeOfCongestion,
            TypeOfJourneyPattern,
            TypeOfLine,
            TypeOfActivation,
            TypeOfDeliveryVariant,
            TypeOfNotice,
            TypeOfFacility,
            TypeOfService,
            TypeOfEquipment,
            TypeOfFeature,
            TypeOfLinkSequence,
            TypeOfPlace,
            TypeOfTransfer,
            TypeOfOperation,
            TypeOfOrganisationPart,
            TypeOfOrganisation,
            TypeOfZone,
            TypeOfLink,
            TypeOfPoint,
            TypeOfProjection,
            TypeOfFrame,
            TypeOfResponsibilityRole,
            TypeOfEntity,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfRetailDevice",
                    "type": TypeOfRetailDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountStatus",
                    "type": CustomerAccountStatus,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCustomerAccount",
                    "type": TypeOfCustomerAccount,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContractEntry",
                    "type": TypeOfFareContractEntry,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContract",
                    "type": TypeOfFareContract,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTravelDocument",
                    "type": TypeOfTravelDocument,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSalesOfferPackage",
                    "type": TypeOfSalesOfferPackage,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareProduct",
                    "type": TypeOfFareProduct,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureElement",
                    "type": TypeOfFareStructureElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTariff",
                    "type": TypeOfTariff,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfAccessRightAssignment",
                    "type": TypeOfAccessRightAssignment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureFactor",
                    "type": TypeOfFareStructureFactor,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFlexibleService",
                    "type": TypeOfFlexibleService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTimeDemandType",
                    "type": TypeOfTimeDemandType,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPassengerInformationEquipment",
                    "type": TypeOfPassengerInformationEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCongestion",
                    "type": TypeOfCongestion,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfJourneyPattern",
                    "type": TypeOfJourneyPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLine",
                    "type": TypeOfLine,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfActivation",
                    "type": TypeOfActivation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDeliveryVariant",
                    "type": TypeOfDeliveryVariant,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfNotice",
                    "type": TypeOfNotice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFacility",
                    "type": TypeOfFacility,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfService",
                    "type": TypeOfService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEquipment",
                    "type": TypeOfEquipment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFeature",
                    "type": TypeOfFeature,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLinkSequence",
                    "type": TypeOfLinkSequence,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPlace",
                    "type": TypeOfPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTransfer",
                    "type": TypeOfTransfer,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOperation",
                    "type": TypeOfOperation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisationPart",
                    "type": TypeOfOrganisationPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisation",
                    "type": TypeOfOrganisation,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfZone",
                    "type": TypeOfZone,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLink",
                    "type": TypeOfLink,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPoint",
                    "type": TypeOfPoint,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProjection",
                    "type": TypeOfProjection,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFrame",
                    "type": TypeOfFrame,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfResponsibilityRole",
                    "type": TypeOfResponsibilityRole,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEntity",
                    "type": TypeOfEntity,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
