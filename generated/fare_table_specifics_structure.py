from dataclasses import dataclass, field
from typing import Optional, Union

from generated.class_of_use_ref import ClassOfUseRef
from generated.distribution_channel_ref import DistributionChannelRef
from generated.facility_set_ref import FacilitySetRef
from generated.fare_class import FareClass
from generated.fare_section_ref import FareSectionRef
from generated.flexible_line_ref import FlexibleLineRef
from generated.group_of_distribution_channels_ref import (
    GroupOfDistributionChannelsRef,
)
from generated.group_of_lines_ref import GroupOfLinesRef
from generated.group_of_services_ref import GroupOfServicesRef
from generated.line_ref import LineRef
from generated.network_ref import NetworkRef
from generated.operator_ref import OperatorRef
from generated.parking_ref import ParkingRef
from generated.payment_method_enumeration import PaymentMethodEnumeration
from generated.point_of_interest_ref import PointOfInterestRef
from generated.relative_direction_enumeration import (
    RelativeDirectionEnumeration,
)
from generated.routing_type_enumeration import RoutingTypeEnumeration
from generated.service_facility_set_ref import ServiceFacilitySetRef
from generated.service_journey_ref import ServiceJourneyRef
from generated.service_site_ref import ServiceSiteRef
from generated.site_facility_set_ref import SiteFacilitySetRef
from generated.site_ref import SiteRef
from generated.stop_place_ref import StopPlaceRef
from generated.tariff_zone_ref import TariffZoneRef
from generated.template_service_journey_ref import TemplateServiceJourneyRef
from generated.train_number_ref import TrainNumberRef
from generated.type_of_fare_product_ref import TypeOfFareProductRef
from generated.type_of_payment_method_ref import TypeOfPaymentMethodRef
from generated.type_of_product_category_ref import TypeOfProductCategoryRef
from generated.type_of_service_ref import TypeOfServiceRef
from generated.type_of_travel_document_ref import TypeOfTravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FareTableSpecificsStructure:
    """
    Specific references for FARE TABLE.

    :ivar operator_ref:
    :ivar network_ref_or_group_of_lines_ref:
    :ivar flexible_line_ref_or_line_ref:
    :ivar choice:
    :ivar tariff_zone_ref:
    :ivar fare_section_ref:
    :ivar direction_type: For fares for DISTANCE MATRIXE LEMENTs,
        DIRECTION in which price applies.
    :ivar routing_type: Whether fare is for s a direct i.e. no changes
        required point to point  fare or indirect routing.
    :ivar fare_class:
    :ivar class_of_use_ref:
    :ivar
        service_facility_set_ref_or_site_facility_set_ref_or_facility_set_ref:
    :ivar type_of_product_category_ref:
    :ivar type_of_service_ref:
    :ivar choice_1:
    :ivar type_of_fare_product_ref:
    :ivar
        distribution_channel_ref_or_group_of_distribution_channels_ref:
    :ivar payment_method: Preferred payment Method .
    :ivar type_of_payment_method_ref:
    :ivar type_of_travel_document_ref:
    """

    operator_ref: Optional[OperatorRef] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    network_ref_or_group_of_lines_ref: Optional[
        Union[NetworkRef, GroupOfLinesRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
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
    flexible_line_ref_or_line_ref: Optional[
        Union[FlexibleLineRef, LineRef]
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
            ),
        },
    )
    choice: Optional[
        Union[
            StopPlaceRef,
            ParkingRef,
            PointOfInterestRef,
            ServiceSiteRef,
            SiteRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "StopPlaceRef",
                    "type": StopPlaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingRef",
                    "type": ParkingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PointOfInterestRef",
                    "type": PointOfInterestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceSiteRef",
                    "type": ServiceSiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteRef",
                    "type": SiteRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    tariff_zone_ref: Optional[TariffZoneRef] = field(
        default=None,
        metadata={
            "name": "TariffZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_section_ref: Optional[FareSectionRef] = field(
        default=None,
        metadata={
            "name": "FareSectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    direction_type: Optional[RelativeDirectionEnumeration] = field(
        default=None,
        metadata={
            "name": "DirectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    routing_type: Optional[RoutingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RoutingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_class: Optional[FareClass] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_use_ref: Optional[ClassOfUseRef] = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_facility_set_ref_or_site_facility_set_ref_or_facility_set_ref: Optional[
        Union[ServiceFacilitySetRef, SiteFacilitySetRef, FacilitySetRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ServiceFacilitySetRef",
                    "type": ServiceFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SiteFacilitySetRef",
                    "type": SiteFacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FacilitySetRef",
                    "type": FacilitySetRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_product_category_ref: Optional[TypeOfProductCategoryRef] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_service_ref: Optional[TypeOfServiceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice_1: Optional[
        Union[
            TemplateServiceJourneyRef,
            ServiceJourneyRef,
            TrainNumberRef,
            GroupOfServicesRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TemplateServiceJourneyRef",
                    "type": TemplateServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ServiceJourneyRef",
                    "type": ServiceJourneyRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainNumberRef",
                    "type": TrainNumberRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfServicesRef",
                    "type": GroupOfServicesRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    type_of_fare_product_ref: Optional[TypeOfFareProductRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareProductRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distribution_channel_ref_or_group_of_distribution_channels_ref: Optional[
        Union[DistributionChannelRef, GroupOfDistributionChannelsRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistributionChannelRef",
                    "type": DistributionChannelRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfDistributionChannelsRef",
                    "type": GroupOfDistributionChannelsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    payment_method: Optional[PaymentMethodEnumeration] = field(
        default=None,
        metadata={
            "name": "PaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_payment_method_ref: Optional[TypeOfPaymentMethodRef] = field(
        default=None,
        metadata={
            "name": "TypeOfPaymentMethodRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_travel_document_ref: Optional[TypeOfTravelDocumentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
