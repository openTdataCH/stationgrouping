from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from xsdata.models.datatype import XmlDateTime

from generated.capping_rule_price_ref import CappingRulePriceRef
from generated.cell_ref import CellRef
from generated.controllable_element_price_ref import (
    ControllableElementPriceRef,
)
from generated.customer_purchase_package_price_ref import (
    CustomerPurchasePackagePriceRef,
)
from generated.distance_matrix_element_price_ref import (
    DistanceMatrixElementPriceRef,
)
from generated.fare_contract_entry_version_structure import (
    FareContractEntryVersionStructure,
)
from generated.fare_price_ref import FarePriceRef
from generated.fare_product_price_ref import FareProductPriceRef
from generated.fare_request_ref import FareRequestRef
from generated.fare_structure_element_price_ref import (
    FareStructureElementPriceRef,
)
from generated.fulfilment_method_price_ref import FulfilmentMethodPriceRef
from generated.geographical_interval_price_ref import (
    GeographicalIntervalPriceRef,
)
from generated.geographical_unit_price_ref import GeographicalUnitPriceRef
from generated.notice_assignments_rel_structure import (
    NoticeAssignmentsRelStructure,
)
from generated.parking_price_ref import ParkingPriceRef
from generated.payment_method_enumeration import PaymentMethodEnumeration
from generated.price_rule_step_results_rel_structure import (
    PriceRuleStepResultsRelStructure,
)
from generated.price_unit_ref import PriceUnitRef
from generated.quality_structure_factor_price_ref import (
    QualityStructureFactorPriceRef,
)
from generated.repeated_trip_fare_request_ref import RepeatedTripFareRequestRef
from generated.sales_offer_package_price_ref import SalesOfferPackagePriceRef
from generated.sales_transaction_ref import SalesTransactionRef
from generated.schedule_request_ref import ScheduleRequestRef
from generated.series_constraint_price_ref import SeriesConstraintPriceRef
from generated.single_trip_fare_request_ref import SingleTripFareRequestRef
from generated.specific_parameter_assignments_rel_structure import (
    SpecificParameterAssignmentsRelStructure,
)
from generated.stop_event_request_ref import StopEventRequestRef
from generated.stop_finder_request_ref import StopFinderRequestRef
from generated.time_interval_price_ref import TimeIntervalPriceRef
from generated.time_unit_price_ref import TimeUnitPriceRef
from generated.travel_specification_summary_view import (
    TravelSpecificationSummaryView,
)
from generated.trip_plan_request_ref import TripPlanRequestRef
from generated.type_of_payment_method_ref import TypeOfPaymentMethodRef
from generated.usage_parameter_price_ref import UsageParameterPriceRef
from generated.validable_element_price_ref import ValidableElementPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelSpecificationVersionStructure(FareContractEntryVersionStructure):
    """
    Type for TRAVEL SPECIFICATION.

    :ivar sales_transaction_ref:
    :ivar choice:
    :ivar choice_1:
    :ivar amount: PRICE amount. in specified currency.
    :ivar currency: Currency of Price ISO 4217.
    :ivar price_unit_ref:
    :ivar units: Other units for PRICE (If not in a currency).
    :ivar rule_step_results: Interim amounts for any pricing rules
        applied to derive price , for example VAT amount  charged.
        +v1.1
    :ivar payment_method: Method of payment used,
    :ivar type_of_payment_method_ref:
    :ivar start_of_validity: Start Validity of Purchased PRODUCT.
    :ivar end_of_validity: End Validity of Purchased PRODUCT.
    :ivar travel_specification_summary_view: Summary of key aspects of
        TRAVEL SPECIFICATION. +V1.1. This data should all be derivable
        from the detailed parameter assignments of the v+1.1
    :ivar specific_parameter_assignments: SPECIFIC PARAMETER ASSIGNMENTS
        for  TRAVEL SPECIFICATION.
    :ivar notice_assignments: NOTICE  ASSIGNMENTS  applying to TRAVEL
        SPECIFICATION.
    """

    class Meta:
        name = "TravelSpecification_VersionStructure"

    sales_transaction_ref: Optional[SalesTransactionRef] = field(
        default=None,
        metadata={
            "name": "SalesTransactionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    choice: Optional[
        Union[
            RepeatedTripFareRequestRef,
            SingleTripFareRequestRef,
            FareRequestRef,
            StopFinderRequestRef,
            StopEventRequestRef,
            ScheduleRequestRef,
            TripPlanRequestRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "RepeatedTripFareRequestRef",
                    "type": RepeatedTripFareRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SingleTripFareRequestRef",
                    "type": SingleTripFareRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareRequestRef",
                    "type": FareRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopFinderRequestRef",
                    "type": StopFinderRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "StopEventRequestRef",
                    "type": StopEventRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduleRequestRef",
                    "type": ScheduleRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TripPlanRequestRef",
                    "type": TripPlanRequestRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    choice_1: Optional[
        Union[
            CustomerPurchasePackagePriceRef,
            ParkingPriceRef,
            TimeIntervalPriceRef,
            TimeUnitPriceRef,
            QualityStructureFactorPriceRef,
            ControllableElementPriceRef,
            ValidableElementPriceRef,
            GeographicalIntervalPriceRef,
            GeographicalUnitPriceRef,
            UsageParameterPriceRef,
            SalesOfferPackagePriceRef,
            DistanceMatrixElementPriceRef,
            FareStructureElementPriceRef,
            FulfilmentMethodPriceRef,
            SeriesConstraintPriceRef,
            CappingRulePriceRef,
            FareProductPriceRef,
            FarePriceRef,
            CellRef,
        ]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CustomerPurchasePackagePriceRef",
                    "type": CustomerPurchasePackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPriceRef",
                    "type": ParkingPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeIntervalPriceRef",
                    "type": TimeIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TimeUnitPriceRef",
                    "type": TimeUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "QualityStructureFactorPriceRef",
                    "type": QualityStructureFactorPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ControllableElementPriceRef",
                    "type": ControllableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ValidableElementPriceRef",
                    "type": ValidableElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalIntervalPriceRef",
                    "type": GeographicalIntervalPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPriceRef",
                    "type": GeographicalUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageParameterPriceRef",
                    "type": UsageParameterPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SalesOfferPackagePriceRef",
                    "type": SalesOfferPackagePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DistanceMatrixElementPriceRef",
                    "type": DistanceMatrixElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementPriceRef",
                    "type": FareStructureElementPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FulfilmentMethodPriceRef",
                    "type": FulfilmentMethodPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SeriesConstraintPriceRef",
                    "type": SeriesConstraintPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappingRulePriceRef",
                    "type": CappingRulePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductPriceRef",
                    "type": FareProductPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePriceRef",
                    "type": FarePriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Amount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    currency: Optional[str] = field(
        default=None,
        metadata={
            "name": "Currency",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_length": 3,
            "max_length": 3,
            "pattern": r"[A-Z][A-Z][A-Z]",
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
    units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Units",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rule_step_results: Optional[PriceRuleStepResultsRelStructure] = field(
        default=None,
        metadata={
            "name": "ruleStepResults",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    start_of_validity: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartOfValidity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_of_validity: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "EndOfValidity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    travel_specification_summary_view: Optional[
        TravelSpecificationSummaryView
    ] = field(
        default=None,
        metadata={
            "name": "TravelSpecificationSummaryView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    specific_parameter_assignments: Optional[
        SpecificParameterAssignmentsRelStructure
    ] = field(
        default=None,
        metadata={
            "name": "specificParameterAssignments",
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
