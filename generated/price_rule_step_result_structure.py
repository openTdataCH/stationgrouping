from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from generated.capping_rule_price_ref import CappingRulePriceRef
from generated.controllable_element_price_ref import (
    ControllableElementPriceRef,
)
from generated.customer_purchase_package_price_ref import (
    CustomerPurchasePackagePriceRef,
)
from generated.discounting_rule_ref import DiscountingRuleRef
from generated.distance_matrix_element_price_ref import (
    DistanceMatrixElementPriceRef,
)
from generated.fare_price_ref import FarePriceRef
from generated.fare_product_price_ref import FareProductPriceRef
from generated.fare_structure_element_price_ref import (
    FareStructureElementPriceRef,
)
from generated.fulfilment_method_price_ref import FulfilmentMethodPriceRef
from generated.geographical_interval_price_ref import (
    GeographicalIntervalPriceRef,
)
from generated.geographical_unit_price_ref import GeographicalUnitPriceRef
from generated.limiting_rule_ref import LimitingRuleRef
from generated.multilingual_string import MultilingualString
from generated.parking_price_ref import ParkingPriceRef
from generated.price_unit_ref import PriceUnitRef
from generated.pricing_rule_ref import PricingRuleRef
from generated.quality_structure_factor_price_ref import (
    QualityStructureFactorPriceRef,
)
from generated.rounding_ref import RoundingRef
from generated.rounding_step_ref import RoundingStepRef
from generated.sales_offer_package_price_ref import SalesOfferPackagePriceRef
from generated.series_constraint_price_ref import SeriesConstraintPriceRef
from generated.time_interval_price_ref import TimeIntervalPriceRef
from generated.time_unit_price_ref import TimeUnitPriceRef
from generated.usage_parameter_price_ref import UsageParameterPriceRef
from generated.validable_element_price_ref import ValidableElementPriceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PriceRuleStepResultStructure:
    """
    Type for FARE STEP RESULT.

    :ivar choice:
    :ivar amount: PRICE amount. in specified currency.
    :ivar currency: Currency of Price ISO 4217.
    :ivar price_unit_ref:
    :ivar units: Other units for PRICE (If not in a currency).
    :ivar rate_used: Discount rate used .
    :ivar adjustment_amount: Step calculation amount,  in same currency
        as STEP RESULT Amount. ( i.e. difference between  Base Amount
        and result Amount. PRICE) +v1.1
    :ivar adjustment_units: Step calculation Units,  in same  PRICE UNIT
        as STEP RESULT Amount.  ( i.e. difference between base Units and
        Result Units. +v1.1
    :ivar limiting_rule_ref_or_discounting_rule_ref_or_pricing_rule_ref:
    :ivar rounding_ref:
    :ivar rounding_step_ref:
    :ivar narrative: Explanation of calcuation step as text.  +v1.1
    :ivar id: Identifier of PriceRuleStepResult
    :ivar order: Order of step.
    """

    choice: Optional[
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
    rate_used: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "RateUsed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    adjustment_amount: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AdjustmentAmount",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    adjustment_units: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "AdjustmentUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    limiting_rule_ref_or_discounting_rule_ref_or_pricing_rule_ref: Optional[
        Union[LimitingRuleRef, DiscountingRuleRef, PricingRuleRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "LimitingRuleRef",
                    "type": LimitingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DiscountingRuleRef",
                    "type": DiscountingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PricingRuleRef",
                    "type": PricingRuleRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
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
    rounding_step_ref: Optional[RoundingStepRef] = field(
        default=None,
        metadata={
            "name": "RoundingStepRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    narrative: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Narrative",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
