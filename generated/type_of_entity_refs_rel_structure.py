from dataclasses import dataclass, field
from typing import List, Union

from generated.all_distribution_channels_ref import AllDistributionChannelsRef
from generated.customer_account_status_ref import CustomerAccountStatusRef
from generated.one_to_many_relationship_structure import (
    OneToManyRelationshipStructure,
)
from generated.type_of_access_right_assignment_ref import (
    TypeOfAccessRightAssignmentRef,
)
from generated.type_of_congestion_ref import TypeOfCongestionRef
from generated.type_of_customer_account_ref import TypeOfCustomerAccountRef
from generated.type_of_delivery_variant_ref import TypeOfDeliveryVariantRef
from generated.type_of_equipment_ref import TypeOfEquipmentRef
from generated.type_of_facility_ref import TypeOfFacilityRef
from generated.type_of_fare_contract_entry_ref import (
    TypeOfFareContractEntryRef,
)
from generated.type_of_fare_contract_ref import TypeOfFareContractRef
from generated.type_of_fare_product_ref import TypeOfFareProductRef
from generated.type_of_fare_structure_element_ref import (
    TypeOfFareStructureElementRef,
)
from generated.type_of_fare_structure_factor_ref import (
    TypeOfFareStructureFactorRef,
)
from generated.type_of_feature_ref import TypeOfFeatureRef
from generated.type_of_flexible_service_ref import TypeOfFlexibleServiceRef
from generated.type_of_frame_ref import TypeOfFrameRef
from generated.type_of_journey_pattern_ref import TypeOfJourneyPatternRef
from generated.type_of_line_ref import TypeOfLineRef
from generated.type_of_link_ref import TypeOfLinkRef
from generated.type_of_link_sequence_ref import TypeOfLinkSequenceRef
from generated.type_of_machine_readability_ref import (
    TypeOfMachineReadabilityRef,
)
from generated.type_of_notice_ref import TypeOfNoticeRef
from generated.type_of_organisation_part_ref import TypeOfOrganisationPartRef
from generated.type_of_organisation_ref import TypeOfOrganisationRef
from generated.type_of_passenger_information_equipment_ref import (
    TypeOfPassengerInformationEquipmentRef,
)
from generated.type_of_place_ref import TypeOfPlaceRef
from generated.type_of_point_ref import TypeOfPointRef
from generated.type_of_pricing_rule_ref import TypeOfPricingRuleRef
from generated.type_of_projection_ref import TypeOfProjectionRef
from generated.type_of_retail_device_ref import TypeOfRetailDeviceRef
from generated.type_of_sales_offer_package_ref import (
    TypeOfSalesOfferPackageRef,
)
from generated.type_of_security_list_ref import TypeOfSecurityListRef
from generated.type_of_service_feature_ref import TypeOfServiceFeatureRef
from generated.type_of_service_ref import TypeOfServiceRef
from generated.type_of_tariff_ref import TypeOfTariffRef
from generated.type_of_time_demand_type_ref import TypeOfTimeDemandTypeRef
from generated.type_of_transfer_ref import TypeOfTransferRef
from generated.type_of_travel_document_ref import TypeOfTravelDocumentRef
from generated.type_of_validity_ref import TypeOfValidityRef
from generated.type_of_zone_ref import TypeOfZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TypeOfEntityRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of references to a TYPE OF VALUE.
    """

    class Meta:
        name = "typeOfEntityRefs_RelStructure"

    choice: List[
        Union[
            TypeOfRetailDeviceRef,
            CustomerAccountStatusRef,
            TypeOfCustomerAccountRef,
            TypeOfFareContractEntryRef,
            TypeOfFareContractRef,
            TypeOfAccessRightAssignmentRef,
            TypeOfSalesOfferPackageRef,
            TypeOfFareStructureElementRef,
            TypeOfTariffRef,
            AllDistributionChannelsRef,
            TypeOfMachineReadabilityRef,
            TypeOfTravelDocumentRef,
            TypeOfFareProductRef,
            TypeOfFareStructureFactorRef,
            TypeOfPricingRuleRef,
            TypeOfFlexibleServiceRef,
            TypeOfPassengerInformationEquipmentRef,
            TypeOfServiceFeatureRef,
            TypeOfCongestionRef,
            TypeOfTimeDemandTypeRef,
            TypeOfJourneyPatternRef,
            TypeOfSecurityListRef,
            TypeOfDeliveryVariantRef,
            TypeOfNoticeRef,
            TypeOfServiceRef,
            TypeOfFacilityRef,
            TypeOfEquipmentRef,
            TypeOfProjectionRef,
            TypeOfFeatureRef,
            TypeOfLinkSequenceRef,
            TypeOfOrganisationPartRef,
            TypeOfOrganisationRef,
            TypeOfPlaceRef,
            TypeOfTransferRef,
            TypeOfZoneRef,
            TypeOfLinkRef,
            TypeOfPointRef,
            TypeOfLineRef,
            TypeOfValidityRef,
            TypeOfFrameRef,
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TypeOfRetailDeviceRef",
                    "type": TypeOfRetailDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CustomerAccountStatusRef",
                    "type": CustomerAccountStatusRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCustomerAccountRef",
                    "type": TypeOfCustomerAccountRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContractEntryRef",
                    "type": TypeOfFareContractEntryRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareContractRef",
                    "type": TypeOfFareContractRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfAccessRightAssignmentRef",
                    "type": TypeOfAccessRightAssignmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSalesOfferPackageRef",
                    "type": TypeOfSalesOfferPackageRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureElementRef",
                    "type": TypeOfFareStructureElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTariffRef",
                    "type": TypeOfTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AllDistributionChannelsRef",
                    "type": AllDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfMachineReadabilityRef",
                    "type": TypeOfMachineReadabilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTravelDocumentRef",
                    "type": TypeOfTravelDocumentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareProductRef",
                    "type": TypeOfFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFareStructureFactorRef",
                    "type": TypeOfFareStructureFactorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPricingRuleRef",
                    "type": TypeOfPricingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFlexibleServiceRef",
                    "type": TypeOfFlexibleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPassengerInformationEquipmentRef",
                    "type": TypeOfPassengerInformationEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfServiceFeatureRef",
                    "type": TypeOfServiceFeatureRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfCongestionRef",
                    "type": TypeOfCongestionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTimeDemandTypeRef",
                    "type": TypeOfTimeDemandTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfJourneyPatternRef",
                    "type": TypeOfJourneyPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfSecurityListRef",
                    "type": TypeOfSecurityListRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfDeliveryVariantRef",
                    "type": TypeOfDeliveryVariantRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfNoticeRef",
                    "type": TypeOfNoticeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfServiceRef",
                    "type": TypeOfServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFacilityRef",
                    "type": TypeOfFacilityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfEquipmentRef",
                    "type": TypeOfEquipmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfProjectionRef",
                    "type": TypeOfProjectionRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFeatureRef",
                    "type": TypeOfFeatureRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLinkSequenceRef",
                    "type": TypeOfLinkSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisationPartRef",
                    "type": TypeOfOrganisationPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfOrganisationRef",
                    "type": TypeOfOrganisationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPlaceRef",
                    "type": TypeOfPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfTransferRef",
                    "type": TypeOfTransferRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfZoneRef",
                    "type": TypeOfZoneRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLinkRef",
                    "type": TypeOfLinkRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfPointRef",
                    "type": TypeOfPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfLineRef",
                    "type": TypeOfLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfValidityRef",
                    "type": TypeOfValidityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TypeOfFrameRef",
                    "type": TypeOfFrameRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
